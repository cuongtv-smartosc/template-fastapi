from settings import logger
from fastapi.routing import APIRouter
from typing import List

from src.crud.charger_model_crud import ChargerModelCrud
from src.models.charger_model import ChargerResponse, ChargerIncoming
from src.schemas.response import resp

charger_model_router = APIRouter()


@charger_model_router.get("s", response_model=List[ChargerResponse])
async def list_charger_model():
    """
    This endpoint interacts with the list charger-model
    """
    logger.info("endpoint list charger-model")
    results, pagination = await ChargerModelCrud().get_all_charger_model()
    return resp.success(data=results, pagination=pagination)


@charger_model_router.post("/create", response_model=List[ChargerResponse])
async def create_charger_model(chargermodel: ChargerIncoming):
    """
    This endpoint interacts with the list charger-model
    """
    logger.info("endpoint create charger-model")
    results = {"item": chargermodel}
    return resp.success(data=results)
