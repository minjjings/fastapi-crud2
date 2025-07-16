from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.api.v1 import user

def create_app():
    app = FastAPI()
    Base.metadata.create_all(bind=engine)
    app.include_router(user.router)
    return app

app = create_app()
