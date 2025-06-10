
from pydantic import BaseModel

# ======================== SCHEMA CHO CUSTOMER ========================

class CustomerCreate(BaseModel):
    name: str
    email: str
    facebook_post: str

class CustomerOut(BaseModel):
    id: int
    name: str
    email: str
    facebook_post: str

    class Config:
        orm_mode = True

# ======================== SCHEMA CHO GIFT ========================

class GiftCreate(BaseModel):
    name: str
    price: int
    description: str

class GiftOut(BaseModel):
    id: int
    name: str
    price: int
    description: str

    class Config:
        orm_mode = True
