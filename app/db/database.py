from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_secret

MYSQL_URL = get_secret("MYSQL_URL")
MYSQL_ECHO = get_secret("MYSQL_ECHO", "false").lower() == "true"
POOL_SIZE = int(get_secret("MYSQL_POOL_SIZE", "10"))
MAX_OVERFLOW = int(get_secret("MYSQL_MAX_OVERFLOW", "20"))

# 데이터베이스 연결을 생성하고 관리하는 객체
engine = create_engine(
    MYSQL_URL,
    echo=MYSQL_ECHO,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
)

# 데이터베이스 세션팩토리
# DB와의 상호작용을 위한 세션 객체를 생성하는 공장
# 실제 쿼리 실행용 세션 인스턴스를 만들 수 있습니다.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
