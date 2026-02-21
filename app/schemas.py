from pydantic import BaseModel , EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name : str
    email : EmailStr
    phone : Optional[str] = None
    address : Optional[str] = None

class UserResponse(UserCreate):
    pass


class ProductCreate(BaseModel):
    sku : str
    name :str
    price : float
    stock: int
    description : Optional[str] = None

class ProductResponse(ProductCreate):
    pass