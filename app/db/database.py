from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
