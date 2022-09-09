from fastapi import APIRouter, Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.handle_error import ValidateException
from app.models.user import User
from app.schemas.electric_vehicle import (
    VehicleGetListFilterString,
    VehicleGetListParams,
)
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.overview_page import vehicle_by_location

vehicle_by_location_router = APIRouter()


@vehicle_by_location_router.get("/")
def vehicle_by_locations(
    params: VehicleGetListParams = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        filters = params.__dict__
        page = filters.get("page")
        number_of_record = filters.get("number_of_record")

        filters = VehicleGetListFilterString(**filters).dict()

        sort_by = filters.get("sort_by")
        sort_order = filters.get("sort_order")

        data = vehicle_by_location(
            page, number_of_record, sort_by, sort_order, db, current_user
        )
        return resp.success(data=data)
    except ValidationError as e:
        raise ValidateException(e.errors())
