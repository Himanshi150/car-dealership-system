from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    is_admin: bool
    class Config:
        from_attributes = True

class VehicleCreate(BaseModel):
    make: str
    model: str
    category: str
    price: float
    quantity: int

class VehicleOut(VehicleCreate):
    id: int
    class Config:
        from_attributes = True