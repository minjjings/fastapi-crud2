# app/models/user.py
# 사용자 모델을 정의하는 파일입니다.
# SQLAlchemy를 사용하여 데이터베이스 테이블과 매핑합니다.
# 이 파일은 사용자 관련 데이터베이스 모델을 정의합니다.


from sqlalchemy import Column, Integer, String
from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
