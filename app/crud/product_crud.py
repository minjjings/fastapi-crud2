from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

# 영화 생성 함수
def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        is_active=True
        
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 영화 목록 조회 함수
# def get_movies(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Movie).offset(skip).limit(limit).all()
# # 특정 영화 조회 함수
# def get_movie(db: Session, movie_id: int):
#     return db.query(Movie).filter(Movie.id == movie_id).first()

# # 영화 삭제 함수
# def delete_movie(db: Session, movie_id: int):
#     movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if movie:
#         db.delete(movie)
#         db.commit()
#     return movie

# app/crud/movie_crud.py
# 이 파일은 영화 관련 CRUD 작업을 정의합니다.