from pydantic import BaseModel

class MovieCreate(BaseModel):
    
    title: str
    director: str
    release_year: int
    genre: str = None
    rating: int = None
    description: str = None


class MovieRead(BaseModel):
    id: int
    title: str
    director: str
    release_year: int
    genre: str = None
    rating: int = None
    description: str = None

    class Config:
        orm_mode = True  # SQLAlchemy 모델과 호환되도록 설정합니다.