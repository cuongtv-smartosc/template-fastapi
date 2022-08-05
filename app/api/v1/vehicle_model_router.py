from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.handle_error import BadRequestException, NotFoundException
from app.crud.vehicle_model_crud import vehicle_model_crud
from app.schemas.electric_vehicle_model import VehicleModelCreate
from app.schemas.response import resp

vehicle_model = APIRouter()


# api get list
@vehicle_model.get("/")
async def get_list_models(db: Session = Depends(get_db)):
    results = await vehicle_model_crud.list(db)
    return resp.success(data=results)


@vehicle_model.get("/{id}")
async def get_detail_model(id: str, db: Session = Depends(get_db)):
    results = await vehicle_model_crud.get(db, id)
    if not results:
        raise NotFoundException(message="Model Not Found")
    return resp.success(data=results)


@vehicle_model.post("/")
async def create_model(
    request: VehicleModelCreate, db: Session = Depends(get_db)
) -> str:
    model = await vehicle_model_crud.get(db, request.__dict__["name"])
    if model:
        raise BadRequestException(message="Name already exists")
    await vehicle_model_crud.create(db=db, obj_in=request)
    return "Successful new creation"
