import io
import logging
import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.config import settings
from src.db.config_db_peewee import db
from src.db.config_db_sqlalchemy import DBBaseCustom, engine
from src.models.charger_model import ChargerModel
from src.router.v1_router import api_v1_router


def create_app() -> FastAPI:
    """
    Create object FatAPI
    :return:
    """
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
    )

    register_cors(app)

    register_router(app)

    register_exception(app)

    register_init(app)

    create_tables()

    return app


def create_tables():
    DBBaseCustom.metadata.create_all(bind=engine)
    db.create_tables([ChargerModel])


def register_router(app: FastAPI) -> None:
    """
    Register route
    :param app:
    :return:
    """
    app.include_router(api_v1_router)


def register_cors(app: FastAPI) -> None:
    """
    Register cors
    :param app:
    :return:
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_exception(app: FastAPI) -> None:
    """
    Register exception
    exception_handler
    exception_handlers
    TypeError: 'dict' object is not callable
    :param app:
    :return:
    """
    pass


def register_init(app: FastAPI) -> None:
    """
    initialize connection
    :param app:
    :return:
    """

    # @app.on_event("startup")
    # async def init_connect():
    #     db.connect()

    @app.on_event('shutdown')
    async def shutdown_connect():
        if not db.is_closed():
            db.close()
