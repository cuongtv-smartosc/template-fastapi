from fastapi import FastAPI
import io
import os
from settings import ENVIRONMENT, logger
from src.db.config_db_sqlalchemy import engine, DBBaseCustom
from src.router import router
from fastapi.middleware.cors import CORSMiddleware

logger.info(f"ENVIRONMENT={ENVIRONMENT}")


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
            os.path.join(os.path.dirname(__file__), *paths),
            encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def create_tables():
    DBBaseCustom.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(router)


def start_application():
    app = FastAPI(
        title="Template FastApi",
        description="Template fast api",
        version=read("VERSION"),
    )
    origins = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    # create_tables()
    return app


app = start_application()
