from app.db.database import mysqldb
from sqlalchemy.orm import Session

def get_db():
    db = mysqldb.sessionmaker()
    try:
        yield db
    finally:
        db.close()
