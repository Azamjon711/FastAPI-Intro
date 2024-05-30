from pydantic import BaseModel
from typing import Optional


class RegisterModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Azamjon",
                "last_name": "Ahmadjonov",
                "username": "azamjon",
                "password": "******",
                "email": "example@gmail.com",
                "is_staff": True,
                "is_active": True
            }
        }


class LoginModel(BaseModel):
    username: str
    password: str


class CategoryModel(BaseModel):
    id: Optional[int]
    name: str


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float
    category_id: Optional[int]


class OrderModel(BaseModel):
    id: Optional[int]
    user_id: int
    product_id: int