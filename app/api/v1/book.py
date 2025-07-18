from fastapi import APIRouter, Query
# APIRouter를 사용하여 사용자 관련 API 엔드포인트를 정의하는 파일입니다.
# Depends를 사용하여 의존성 주입을 처리합니다.
# HTTPException을 사용하여 오류 처리를 수행합니다.
from fastapi import APIRouter, Depends, HTTPException
# SQLAlchemy의 Session을 사용하여 데이터베이스 세션을 관리합니다.
from sqlalchemy.orm import Session
# app/crud.user 모듈에서 정의한 CRUD 함수들을 사용하여 데이터베이스 작업을 수행합니다.
from app.crud import book_crud
from app.db.database import SessionLocal
# app/core.deps 모듈에서 정의한 get_db 함수를 사용하여 데이터베이스 세션을 주입합니다.
from app.core.deps import get_db
from app.schemas.book import BookCreate, BookRead

from app.crud.book_crud import create_book
router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/",response_model=BookRead)
def read_books(book : BookCreate , db: Session = Depends(get_db)):
    return book_crud.create_book(db, book)

@router.get("/", response_model=list[BookRead])
def get_books(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    return book_crud.get_books(db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = book_crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = book_crud.delete_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}

    