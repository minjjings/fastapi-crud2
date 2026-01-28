# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 1. 아래 임포트 추가
from sqlalchemy.ext.declarative import declarative_base 
from app.core.config import get_secret

MYSQL_URL = get_secret("MYSQL_URL")
MYSQL_ECHO = get_secret("MYSQL_ECHO", "false").lower() == "true"
POOL_SIZE = int(get_secret("MYSQL_POOL_SIZE", "10"))
MAX_OVERFLOW = int(get_secret("MYSQL_MAX_OVERFLOW", "20"))

engine = create_engine(
    MYSQL_URL,
    echo=MYSQL_ECHO,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. 이 줄을 반드시 추가해야 합니다! 
# 모든 Entity(Product, User 등)가 이 Base를 상속받아야 테이블이 생성됩니다.
Base = declarative_base()