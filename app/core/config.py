import os
from dotenv import load_dotenv

# app/core/config.py
# 환경 변수 파일을 로드합니다.

load_dotenv()

# 비밀 정보를 가져오는 함수
# 환경 변수에서 비밀 정보를 가져오는 함수입니다.

def get_secret(key: str, default: str = None):
    return os.getenv(key, default)
