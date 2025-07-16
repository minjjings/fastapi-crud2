import os
from dotenv import load_dotenv

load_dotenv()

def get_secret(key: str, default: str = None):
    return os.getenv(key, default)
