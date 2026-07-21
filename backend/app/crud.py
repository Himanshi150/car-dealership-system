from sqlalchemy.orm import Session
from . import models, schemas, security

# User operations
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=security.hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Vehicle operations
def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(
        make=vehicle.make,
        model=vehicle.model,
        category=vehicle.category,
        price=vehicle.price,
        quantity=vehicle.quantity
    )
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def get_all_vehicles(db: Session):
    return db.query(models.Vehicle).all()

def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

def update_vehicle(db: Session, vehicle_id: int, vehicle: schemas.VehicleCreate):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle:
        db_vehicle.make = vehicle.make
        db_vehicle.model = vehicle.model
        db_vehicle.category = vehicle.category
        db_vehicle.price = vehicle.price
        db_vehicle.quantity = vehicle.quantity
        db.commit()
        db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle:
        db.delete(db_vehicle)
        db.commit()
        return True
    return False

def search_vehicles(db: Session, make: str = None, model: str = None, category: str = None, min_price: float = None, max_price: float = None):
    query = db.query(models.Vehicle)
    if make:
        query = query.filter(models.Vehicle.make.ilike(f"%{make}%"))
    if model:
        query = query.filter(models.Vehicle.model.ilike(f"%{model}%"))
    if category:
        query = query.filter(models.Vehicle.category.ilike(f"%{category}%"))
    if min_price is not None:
        query = query.filter(models.Vehicle.price >= min_price)
    if max_price is not None:
        query = query.filter(models.Vehicle.price <= max_price)
    return query.all()

def purchase_vehicle(db: Session, vehicle_id: int, quantity: int):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle:
        db_vehicle.quantity -= quantity
        db.commit()
        db.refresh(db_vehicle)
    return db_vehicle

def restock_vehicle(db: Session, vehicle_id: int, quantity: int):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle:
        db_vehicle.quantity += quantity
        db.commit()
        db.refresh(db_vehicle)
    return db_vehicle