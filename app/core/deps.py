# app/core/deps.py


# 데이터베이스 세션을 주입하기 위한 의존성 함수입니다.
# FastAPI의 Depends를 사용하여 데이터베이스 세션을 관리합니다.
from app.db.database import SessionLocal
# SQLAlchemy의 Session을 사용하여 데이터베이스 세션을 관리합니다.
from sqlalchemy.orm import Session


# get_db 함수는 FastAPI의 의존성 주입 시스템을 사용하여
# 데이터베이스 세션을 생성하고 반환합니다.
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
