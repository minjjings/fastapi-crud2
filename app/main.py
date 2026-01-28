from fastapi import FastAPI
from app.db.database import engine, Base 

# 1. 모델 임포트 (테이블 자동 생성을 위해 필수)
from app.models.user import User
from app.models.book import Book
from app.models.movie import Movie
from app.models.product import Product

# 2. API 라우터 임포트
from app.api.v1 import user, book, movie, product

def create_app():
    # FastAPI 인스턴스 생성
    app = FastAPI(title="FastAPI CRUD Project", version="1.0.0")
    
    # 3. DB 테이블 생성 (이미 있으면 건너뜁니다)
    Base.metadata.create_all(bind=engine)
    
    # 4. 라우터 등록 (이 부분이 빠지면 404가 발생합니다)
    app.include_router(user.router) 
    app.include_router(book.router)
    app.include_router(movie.router)    
    app.include_router(product.router)
    
    # 루트 경로 확인용 (브라우저 접속 시 404 방지)
    @app.get("/")
    def read_root():
        return {"message": "Server is running!"}
        
    return app

# 최종 애플리케이션 객체 생성
app = create_app()