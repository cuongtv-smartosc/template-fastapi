from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.models.user import User
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.electric_vehicle import get_vehicle_list

vehicle_router = APIRouter()


@vehicle_router.get("/")
async def get_vehicles(
    filter=None,
    pageSize=None,
    currentPage=None,
    order_by=None,
    current_user: User = Depends(
        get_current_user,
    ),
    db: Session = Depends(get_db),
):
    results = get_vehicle_list(
        filter, pageSize, currentPage, order_by, db, current_user
    )
    return resp.success(data=results)
