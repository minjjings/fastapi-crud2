# 수정 전
from sqlalchemy import Column, Integer, String, Float

# 수정 후 (Boolean을 추가하세요)
from sqlalchemy import Column, Integer, String, Float, Boolean 
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Integer, default=0)
    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True) # 이제 Boolean을 인식합니다!