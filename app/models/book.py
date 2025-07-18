from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    publisher = Column(String(255))
    price = Column(Integer)
    
