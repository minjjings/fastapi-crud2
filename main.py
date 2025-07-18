from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.api.v1 import user
from app.api.v1 import book
from app.api.v1 import movie

def create_app():
    # FastAPI 애플리케이션 인스턴스를 생성하고 설정합니다.
    app = FastAPI()
    # 데이터베이스 모델을 초기화합니다.
    # Base.metadata.create_all(bind=engine) 는 데이터베이스에 테이블을 생성
    # Base는 SQLAlchemy의 declarative base로, 모든 모델 클래스가 상속받는 기본 클래스입니다.
    # 이 코드는 데이터베이스에 정의된 모든 모델의 테이블을 생성합니다.

    Base.metadata.create_all(bind=engine)
    # 사용자 관련 API 라우터를 애플리케이션에 포함시킵니다.
    app.include_router(user.router) 
    app.include_router(movie.router)
    app.include_router(book.router)   
    # 이 함수는 FastAPI 애플리케이션 인스턴스를 반환합니다.
    
    return app

# FastAPI 애플리케이션을 생성합니다.

app = create_app()
