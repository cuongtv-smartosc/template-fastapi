import math

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.util import vehicles_list_base_filter
from app.models.charger import Charger
from app.models.customer import Customer
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_model import VehicleModel
from app.models.sale_information import SaleInformation
from app.schemas.response import resp

vehicle_router = APIRouter()


@vehicle_router.get("/")
async def get_vehicles(
    filter=None,
    pageSize=None,
    currentPage=None,
    order_by=None,
    db: Session = Depends(get_db),
):
    filters = filter
    page_size = int(pageSize)
    current_page = currentPage
    query = db.query(
        Vehicle.vehicle_number,
        Vehicle.id,
        Vehicle.model_id,
        Vehicle.edge_id,
        Customer.customer_name,
        SaleInformation.sale_type,
    ).filter(
        Vehicle.sale_id == SaleInformation.id,
        SaleInformation.customer_id == Customer.id,
    )
    query = vehicles_list_base_filter(filters, Vehicle.vehicle_number, query)
    total = query.count()
    edges = [i.edge_id for i in query.all()]
    query = query.order_by(Vehicle.vehicle_number.desc())
    if order_by == "asc":
        query = query.order_by(Vehicle.vehicle_number.asc())
    elif order_by == "customer_name":
        query = query.orderby(Vehicle.customer_name.asc())
    offset = (int(current_page) - 1) * int(page_size)
    query = query.limit(page_size).offset(offset).all()
    results = {
        "total": total,
        "currentPage": current_page,
        "totalPage": math.ceil(total / page_size),
        "vehicles": jsonable_encoder(query),
        "list_edge": edges,
    }
    return resp.success(data=results)


@vehicle_router.get("/{id}")
async def get_vehicle_detail(id, db: Session = Depends(get_db)):
    detail = (
        db.query(Vehicle, Charger, VehicleModel)
        .filter(
            Vehicle.charger_id == Charger.id,
            Vehicle.model_id == VehicleModel.id,
            Vehicle.id == id,
        )
        .first()
    )
    data = jsonable_encoder(detail)
    return resp.success(data=data)
