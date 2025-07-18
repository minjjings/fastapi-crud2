# app/crud/user_crud.py

# Session은 SQLQlchemy에서 데이터베이스와 상호작용하기 위한 핵심 객체 
from sqlalchemy.orm import Session

# app.models.user 모듈에서 정의한 User 모델을 사용하여 데이터베이스 작업을 수행합니다.
from app.models.user import User
# app.schemas.user 모듈에서 정의한 Pydantic 모델을 사용하여
# 사용자 생성 요청을 처리합니다.
from app.schemas.user import UserCreate

# 사용자 생성 함수
# db: 데이터베이스 세션 객체
# user: 사용자 생성 요청 데이터
# 이 함수는 새로운 사용자를 데이터베이스에 추가하고,
# 생성된 사용자 객체를 반환합니다.
def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 사용자 조회 함수
# db: 데이터베이스 세션 객체
# skip: 조회할 사용자 목록의 시작 위치 (기본값: 0)
# limit: 조회할 사용자 목록의 최대 개수 (기본값: 10)
# 이 함수는 데이터베이스에서 사용자 목록을 조회하고,
# 조회된 사용자 목록을 반환합니다.
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# 특정 사용자 조회 함수
# db: 데이터베이스 세션 객체
# user_id: 조회할 사용자의 ID
# 이 함수는 데이터베이스에서 특정 사용자를 조회하고,
# 조회된 사용자 객체를 반환합니다. 사용자가 존재하지 않으면 None을 반환합니다.

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# 사용자 삭제 함수
# db: 데이터베이스 세션 객체
# user_id: 삭제할 사용자의 ID
# 이 함수는 데이터베이스에서 특정 사용자를 삭제하고,
# 삭제된 사용자 객체를 반환합니다. 사용자가 존재하지 않으면 None을 반환합니다

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
