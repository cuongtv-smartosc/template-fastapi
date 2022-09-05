from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.common.database import engine
from app.common.handle_error import APIException
from app.config.settings import setting
from app.models.charger import Charger
from app.models.charger_model import ChargerModel
from app.models.company import Company
from app.models.customer import Customer
from app.models.division import Division
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_divison import VehicleDivision
from app.models.electric_vehicle_history import VehicleHistory
from app.models.electric_vehicle_model import VehicleModel
from app.models.sale_information import SaleInformation
from app.models.user import User
from app.models.work_shift import WorkShift
from app.v1_router import api_v1_router


def create_app() -> FastAPI:
    """
    Create object FatAPI
    :return:
    """
    env_yml = setting.get_config_env()
    app = FastAPI(
        title=env_yml.get("TITLE"),
        description=env_yml.get("DESCRIPTION"),
        version=env_yml.get("VERSION"),
        docs_url=None,
    )

    register_cors(app, env_yml)
    register_router(app)
    register_exception(app)
    create_table()
    return app


def create_table():
    User.__table__.create(engine, checkfirst=True)
    ChargerModel.__table__.create(engine, checkfirst=True)
    Charger.__table__.create(engine, checkfirst=True)
    Company.__table__.create(engine, checkfirst=True)
    Customer.__table__.create(engine, checkfirst=True)
    Division.__table__.create(engine, checkfirst=True)
    VehicleModel.__table__.create(engine, checkfirst=True)
    SaleInformation.__table__.create(engine, checkfirst=True)
    Vehicle.__table__.create(engine, checkfirst=True)
    VehicleHistory.__table__.create(engine, checkfirst=True)
    VehicleDivision.__table__.create(engine, checkfirst=True)
    WorkShift.__table__.create(engine, checkfirst=True)


def register_router(app: FastAPI) -> None:
    """
    Register route
    :param app:
    :return:
    """
    app.include_router(api_v1_router)


def register_cors(app: FastAPI, env_yml) -> None:
    """
    Register cors
    :param app:
    :return:
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=env_yml.get("ORIGINS"),
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

    @app.exception_handler(APIException)
    async def unicorn_exception_handler(request: Request, exc: APIException):
        return JSONResponse(
            status_code=exc.http_status,
            content={exc.key_return: exc.message},
        )
