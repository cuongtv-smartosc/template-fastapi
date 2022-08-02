from typing import List

from fastapi import Depends, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.logger import logger
from app.crud.charger_model_crud import charger_model_crud
from app.schemas.charger_model import ChargerModelCreate, ChargerModelResponse
from app.schemas.response import resp

charger_model_router = APIRouter()


@charger_model_router.get("s", response_model=List[ChargerModelResponse])
async def list_charger_model(db: Session = Depends(get_db)):
    """
    This endpoint interacts with the list charger-model
    """
    logger.info("endpoint list charger-model")
    results = await charger_model_crud.list(db)
    return resp.success(data=results)


@charger_model_router.post(
    "/create",
    response_model=List[ChargerModelResponse],
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "docs response api HTTP_422_UNPROCESSABLE_ENTITY"
        },
        status.HTTP_201_CREATED: {
            "content": {
                "application/json": {
                    # "example": {"id": "bar", "value": "The bar tenders"}
                }
            },
        },
    },
    status_code=status.HTTP_201_CREATED,
    name="Name api",
)
async def create_charger_model(charger_model: ChargerModelCreate):
    """
    This endpoint interacts with the create charger-model \n
    """
    logger.info("endpoint create charger-model")
    return resp.success(data=charger_model)
