from typing import List

from fastapi import Depends
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


@charger_model_router.post("/create")
async def create_charger(
    charger: ChargerModelCreate, db: Session = Depends(get_db)
) -> str:
    payload = {**charger.dict()}
    await charger_model_crud.create(db=db, obj_in=payload)
    return payload
