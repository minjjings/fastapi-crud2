from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.movie import MovieCreate, MovieRead
from app.crud import movie_crud
from app.core.deps import get_db

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model = MovieRead)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return movie_crud.create_movie(db, movie)

@router.get("/", response_model=list[MovieRead])
def get_movies(skip: int = 0, limit: int = 10, db:
    Session = Depends(get_db)):
    return movie_crud.get_movies(db, skip=skip, limit=limit)

@router.get("/{movie_id}", response_model=MovieRead)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = movie_crud.get_movie(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = movie_crud.delete_movie(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"detail": "Movie deleted"}
# app/api/v1/movie.py
# 이 파일은 영화 관련 API 엔드포인트를 정의합니다.