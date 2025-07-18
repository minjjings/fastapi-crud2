# app/api/v1/user.py

# APIRouter를 사용하여 사용자 관련 API 엔드포인트를 정의하는 파일입니다.
# Depends를 사용하여 의존성 주입을 처리합니다.
# HTTPException을 사용하여 오류 처리를 수행합니다.
from fastapi import APIRouter, Depends, HTTPException
# SQLAlchemy의 Session을 사용하여 데이터베이스 세션을 관리합니다.
from sqlalchemy.orm import Session
# app/schemas.user 모듈에서 정의한 Pydantic 모델을 사용하여 요청 및 응답 데이터의 유효성을 검사합니다.
from app.schemas.user import UserCreate, UserRead
# app/crud.user 모듈에서 정의한 CRUD 함수들을 사용하여 데이터베이스 작업을 수행합니다.
from app.crud import user_crud
from app.db.database import SessionLocal
# app/core.deps 모듈에서 정의한 get_db 함수를 사용하여 데이터베이스 세션을 주입합니다.
from app.core.deps import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@router.get("/", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db)

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
