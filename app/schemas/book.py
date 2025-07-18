# app/schemas/user.py
# 사용자 관련 데이터 모델을 정의하는 파일입니다.
# Pydantic을 사용하여 데이터 유효성 검사를 수행합니다.
# 이 파일은 사용자 생성 및 조회에 필요한 스키마를 정의합니다.
# Pydantic은 Python의 데이터 모델링 및 유효성 검사 라이브러리입니다.
from pydantic import BaseModel

# 사용자 생성 시 필요한 필드와 데이터 타입을 정의합니다.
# UserCreate는 사용자 생성 요청에 사용되는 모델입니다.
# BaseModel을 상속받아 Pydantic 모델로 정의합니다.

class BookCreate(BaseModel):
    title: str
    publisher: str
    price: int

# 사용자 조회 시 필요한 필드와 데이터 타입을 정의합니다.
# UserRead는 사용자 조회 응답에 사용되는 모델입니다.
# UserRead 모델은 사용자 정보를 반환할 때 사용됩니다.

class BookRead(BaseModel):
    title: str
    publisher: str
    price: int
    

    class Config:
        orm_mode = True

