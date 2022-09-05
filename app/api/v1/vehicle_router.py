import json

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.handle_error import ValidateException
from app.models.user import User
from app.schemas.electric_vehicle import (
    VehicleGetListFilterList,
    VehicleGetListFilterString,
    VehicleGetListParams,
)
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.electric_vehicle import get_vehicle_list

vehicle_router = APIRouter()


@vehicle_router.get("/")
async def get_vehicles(
    params: VehicleGetListParams = Depends(),
    current_user: User = Depends(
        get_current_user,
    ),
    db: Session = Depends(get_db),
):
    try:
        filters = jsonable_encoder(params)
        filters = VehicleGetListFilterList(**filters).dict()
        for key in filters:
            if filters[key] is not None:
                filters[key] = json.loads(filters[key])
        filters.update(VehicleGetListFilterString(**filters).dict())
        results = get_vehicle_list(
            filters=filters,
            current_page=params.current_page,
            page_size=params.page_size,
            order_by=params.order_by,
            db=db,
            current_user=current_user,
        )
        return resp.success(data=results)
    except ValidationError as e:
        raise ValidateException(e.errors())
