from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.common.database import DBBaseCustom, engine
from app.common.handle_error import APIException
from app.config.settings import setting
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
        dependencies=[Depends(get_request_body)]
    )

    register_cors(app, env_yml)
    register_router(app)
    register_exception(app)

    # create_tables()

    return app


def create_tables():
    DBBaseCustom.metadata.create_all(bind=engine)


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
            content={"message": f"{exc.message}"},
        )


async def get_request_body(request: Request):
    if await request.body():
        req_body = await request.json()
        request.state.req_body = req_body
