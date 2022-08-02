from fastapi import Depends, Request
from fastapi.routing import APIRouter
from pydantic.schema import model_schema
from sqlalchemy.orm import Session

from app.common.handle_error import NotFoundException
from app.crud.vehicle_model_crud import vehicle_model_crud
from app.db.config_db_sqlalchemy import get_db
from app.models.electric_vehicle_model import VehicleModel
from app.schemas.electric_vehicle_model import VehicleModelBase, VehicleModelCreate
from app.schemas.response import resp

vehicle_model = APIRouter()


# api get list
@vehicle_model.get("/get_all")
async def get_list_models(db: Session = Depends(get_db)):
    results = await vehicle_model_crud.list(db)

    return resp.success(data=results)


@vehicle_model.get("/get_details/{id}")
async def get_detail_model(id: str, db: Session = Depends(get_db)):
    models = await vehicle_model_crud.list(db)
    if any([model.name == id for model in models]):
        results = await vehicle_model_crud.get(db, id)
        return resp.success(data=results)
    raise NotFoundException(message="Model Not Found")
