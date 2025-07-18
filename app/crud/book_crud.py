from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate

# 책 생성 함수
def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        publisher=book.publisher,
        price=book.price
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 책 목록 조회 함수
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

# 특정 책 조회 함수
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# 책 삭제 함수
def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book