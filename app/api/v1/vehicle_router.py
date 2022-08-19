import json
import math
from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from app.common.database import get_db
from app.common.util import vehicles_list_base_filter

from app.models.electric_vehicle import Vehicle
from app.models.customer import Customer
from app.models.sale_information import SaleInformation
from app.schemas.response import resp

vehicle_router = APIRouter()


@vehicle_router.get("/")
async def get_vehicles(data, db: Session = Depends(get_db)):
    params = json.loads(data)
    filters = params.get('filter')
    page_size = params.get('pageSize')
    current_page = params.get('currentPage')
    query = db.query(Vehicle.vehicle_number, Vehicle.id,
                     Vehicle.model_id,
                     Vehicle.edge_id,
                     Customer.customer_name,
                     SaleInformation.sale_type).filter(Vehicle.sale_id == SaleInformation.id,
                                                       SaleInformation.customer_id == Customer.id)
    query = vehicles_list_base_filter(filters, Vehicle.vehicle_number, query)
    total = query.count()
    edges = [i.edge_id for i in query.all()]
    order_by = query.order_by(Vehicle.vehicle_number.desc())
    if params.get("order_by") == "asc":
        order_by = query.order_by(Vehicle.vehicle_number.asc())
    elif params.get("order_by") == "customer_name":
        order_by = query.orderby(Vehicle.customer_name.asc())

    query = order_by.limit(page_size) \
        .offset((int(current_page) - 1) * int(page_size)) \
        .all()
    results = {
        "total": total,
        "currentPage": current_page,
        "totalPage": math.ceil(total / page_size),
        "data": query,
        "list_edge": edges
    }
    return resp.success(data=results)


@vehicle_router.get("/{id}")
async def get_vehicle_detail(id, db: Session = Depends(get_db)):
    detail = db.query(Vehicle).filter(Vehicle.id == id).first()
    charger = detail.charger.id
    model = detail.vehicle_model.id
    return {"detail": detail}
