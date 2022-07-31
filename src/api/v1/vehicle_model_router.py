from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

# from src.crud.vehicle_model_crud import vehicle_model_crud
# from src.db.config_db_sqlalchemy import get_db

from src.schemas.response import resp

vehicle_model = APIRouter()

#
# @vehicle_model.get("/vehicle-model")
# async def list(db: Session = Depends(get_db)):
#     # results = await vehicle_model_crud.list(db)
#     # print(results)
#     # data = jsonable_encoder(results)
#     # print(data)
#     return resp.success(data=None)
