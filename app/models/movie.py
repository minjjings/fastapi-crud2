from sqlalchemy import Column, Integer, String 
from app.db.base import Base



class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(255),nullable=False)
    director = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=True)
    rating = Column(Integer, nullable=True)
    description = Column(String(500), nullable=True)