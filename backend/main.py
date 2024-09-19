from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
import sys
import sqlalchemy
from apis.base import api_router


# print("SQLAlchemy Version:", sqlalchemy.__version__)
def include_router(app):
    app.include_router(api_router)


def create_tables():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()
print("Python Executable:", sys.executable)
print("Python Path:", sys.path)
print("SQLAlchemy Version:", sqlalchemy.__version__)


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
