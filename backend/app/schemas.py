from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    is_admin: bool
    model_config = ConfigDict(from_attributes=True)

class VehicleCreate(BaseModel):
    make: str
    model: str
    category: str
    price: float
    quantity: int

class VehicleOut(VehicleCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PurchaseRequest(BaseModel):
    quantity: int