from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.models.user import User
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.overview_page import (
    get_total_number_of_contract,
    get_total_number_of_customer,
    get_total_number_of_vehicle,
)

get_total_overview_router = APIRouter()


@get_total_overview_router.get("/total_of_customers")
def get_total_number_of_customers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = get_total_number_of_customer(db, current_user)
    return resp.success(data=data)


@get_total_overview_router.get("/total_of_vehicles")
def get_total_number_of_vehicles(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = get_total_number_of_vehicle(db, current_user)
    return resp.success(data=data)


@get_total_overview_router.get("/total_of_contracts")
def get_total_number_of_contracts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = get_total_number_of_contract(db, current_user)
    return resp.success(data=data)
