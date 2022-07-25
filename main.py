from fastapi import FastAPI
import io
import os
from settings import ENVIRONMENT, logger
from src.router.charger_model_router import charger_model_router
from src.router.index import router as index

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


app = FastAPI(
    title="Template FastApi",
    description="Template fast api",
    version=read("VERSION"),
)

# router index
app.include_router(index)

# router charger model
app.include_router(charger_model_router, prefix="/charger-model")
