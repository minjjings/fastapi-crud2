from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    stock: int

class ProductCreate(ProductBase):
    pass # 등록할 때 받는 데이터

class ProductResponse(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True # SQLAlchemy 객체를 자동으로 Pydantic으로 변환