from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate

# 영화 생성 함수
def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(
        title=movie.title,
        director=movie.director,
        release_year=movie.release_year,
        genre=movie.genre,
        rating=movie.rating,
        description=movie.description
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# 영화 목록 조회 함수
def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Movie).offset(skip).limit(limit).all()
# 특정 영화 조회 함수
def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

# 영화 삭제 함수
def delete_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return movie

# app/crud/movie_crud.py
# 이 파일은 영화 관련 CRUD 작업을 정의합니다.