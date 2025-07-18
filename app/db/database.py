# app/db/database.py
# 데이터베이스 연결 및 세션 관리를 위한 설정 파일입니다.
from sqlalchemy import create_engine
# SQLAlchemy의 세션 팩토리를 생성하기 위한 모듈
# 세션 팩토리란? # SQLAlchemy에서 데이터베이스와 상호작용하기 위한 세션 객체를 생성하는 공장입니다.
from sqlalchemy.orm import sessionmaker
# 환경 변수에서 비밀 정보를 가져오는 함수
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

# autocommit=False: 세션이 커밋될 때까지 변경 사항을 데이터베이스에 반영하지 않습니다.
# autoflush=False: 세션이 커밋되기 전까지 데이터베이스에
# 변경 사항을 자동으로 플러시하지 않습니다.
# bind=engine: 세션이 사용할 데이터베이스 엔진을 지정합니다.
# 이 설정은 데이터베이스와의 연결을 관리하고, 세션을 통해
# 데이터베이스 작업을 수행할 수 있게 합니다.