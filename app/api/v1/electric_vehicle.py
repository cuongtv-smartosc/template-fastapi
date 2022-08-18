import json
import math

from fastapi import Depends

from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_customer import VehicleCustomer
from app.models.electric_vehicle_division import VehicleDivision
from app.models.electric_vehicle_work_shift import VehicleWorkShift


vehicle_router = APIRouter()


@vehicle_router.get("/")
def get_vehicles(data, db: Session = Depends(get_db)):
    electric_vehicle = Vehicle
    params = json.loads(data)
    filters = params.get('filter')
    page_size = params.get('pageSize')
    current_page = params.get('currentPage')
    query = vehicles_list_base_filter(filters, electric_vehicle.vehicle_number, db)
    total = len(query.all())
    edges = [i.edge_id for i in query.all()]
    order_by = query.order_by(electric_vehicle.vehicle_number.desc())
    if params.get("order_by") == "asc":
        order_by = query.order_by(electric_vehicle.vehicle_number.asc())
    elif params.get("order_by") == "customer_name":
        order_by = query.orderby(electric_vehicle.customer_name.asc())

    query = order_by.limit(page_size) \
        .offset((int(current_page) - 1) * int(page_size)) \
        .all()

    return {
        "total": total,
        "currentPage": current_page,
        "totalPage": math.ceil(total / page_size),
        "data": query,
        "list_edge": edges
    }


def vehicles_list_base_filter(params, group_by, db):
    electric_vehicle = Vehicle
    customer = VehicleCustomer
    division = VehicleDivision
    work_shift = VehicleWorkShift
    query = db.query(electric_vehicle.vehicle_number, electric_vehicle.id,
                                   electric_vehicle.model_id,
                                   electric_vehicle.edge_id,
                                   electric_vehicle.customer_id,
                                   electric_vehicle.operation_status
                                   ).join(customer).filter(electric_vehicle.customer_id == customer.id)
    if 'company_name' in params:
        company_name = params['company_name']
        query = query.where(customer.company_name.isin(company_name))

    if 'customer_name' in params:
        query = query.where(electric_vehicle.customer_name.isin(params['customer_name']))

    if 'division_name' in params:
        query = query.inner_join(division).on(electric_vehicle.vehicle_number == division.vehicle_number).where(
            division.vehicle_division.isin(params['division_name']))

    if 'work_shift' in params:
        query = query.inner_join(work_shift).on(electric_vehicle.name == work_shift.vehicle_number)
        work_shifts = params["work_shift"]
        work_shift_names = []
        for item in work_shifts:
            work_shift_name = work_shift.query(work_shift.name).filter(work_shift.work_shift == item.get("shift"),
                                                                       work_shift.work_shift_from == item.get(
                                                                           "ws_from"),
                                                                       work_shift.work_shift_to == item.get(
                                                                           "ws_to")).all()
            data = work_shift_name.run(as_list=True)
            for ws in data:
                work_shift_names.append(ws[0])
        query = query.where(work_shift.name.isin(work_shift_names))

    if 'model_id' in params:
        query = query.where(electric_vehicle.model_id.isin(params['model_id']))

    if 'vehicle_number' in params:
        query = query.where(
            electric_vehicle.vehicle_number.isin(params['vehicle_number']))

    if 'operation_status' in params:
        query = query.where(electric_vehicle.operation_status.isin(
            params['operation_status']))

    if 'sale_id' in params:
        query = query.where(electric_vehicle.sale_id == params.get('sale_id'))

    if 'sale_type' in params:
        query = query.where(electric_vehicle.sale_type == params.get('sale_type'))

    if 'location' in params:
        query = query.where(electric_vehicle.location == params.get('location'))

    if "forklift_pdi_status" in params:
        query = query.where(electric_vehicle.forklift_pdi_status == params.get('forklift_pdi_status'))

    if "sale_order_number" in params:
        query = query.where(electric_vehicle.sale_id == params.get('sale_order_number'))

    if group_by is not None:
        query = query.group_by(group_by)

    return query
