from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import models, schemas, crud, security
from .database import engine, get_db
from .security import get_current_user, require_admin
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth Endpoints
@app.post("/api/auth/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(400, "Email already registered")
    return crud.create_user(db, user)

@app.post("/api/auth/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user or not security.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(401, "Invalid credentials")
    token = security.create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

# Vehicle Endpoints (all protected - require a logged-in user)
@app.post("/api/vehicles", response_model=schemas.VehicleOut)
def create_vehicle(
    vehicle: schemas.VehicleCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.create_vehicle(db, vehicle)

@app.get("/api/vehicles", response_model=list[schemas.VehicleOut])
def get_all_vehicles(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.get_all_vehicles(db)

@app.get("/api/vehicles/search", response_model=list[schemas.VehicleOut])
def search_vehicles(
    make: str = Query(None),
    model: str = Query(None),
    category: str = Query(None),
    min_price: float = Query(None),
    max_price: float = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.search_vehicles(db, make, model, category, min_price, max_price)

@app.get("/api/vehicles/{vehicle_id}", response_model=schemas.VehicleOut)
def get_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    vehicle = crud.get_vehicle(db, vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return vehicle

@app.put("/api/vehicles/{vehicle_id}", response_model=schemas.VehicleOut)
def update_vehicle(
    vehicle_id: int,
    vehicle: schemas.VehicleCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    updated = crud.update_vehicle(db, vehicle_id, vehicle)
    if not updated:
        raise HTTPException(404, "Vehicle not found")
    return updated

# Admin only - delete
@app.delete("/api/vehicles/{vehicle_id}")
def delete_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    deleted = crud.delete_vehicle(db, vehicle_id)
    if not deleted:
        raise HTTPException(404, "Vehicle not found")
    return {"message": "Vehicle deleted"}

# Inventory Endpoints (protected)
@app.post("/api/vehicles/{vehicle_id}/purchase", response_model=schemas.VehicleOut)
def purchase_vehicle(
    vehicle_id: int,
    purchase: schemas.PurchaseRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    vehicle = crud.get_vehicle(db, vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    if vehicle.quantity < purchase.quantity:
        raise HTTPException(400, "Not enough vehicles in stock")
    return crud.purchase_vehicle(db, vehicle_id, purchase.quantity)

# Admin only - restock
@app.post("/api/vehicles/{vehicle_id}/restock", response_model=schemas.VehicleOut)
def restock_vehicle(
    vehicle_id: int,
    restock: schemas.PurchaseRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    vehicle = crud.get_vehicle(db, vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return crud.restock_vehicle(db, vehicle_id, restock.quantity)