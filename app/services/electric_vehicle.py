import math

from fastapi.encoders import jsonable_encoder

from app.common.util import check_role_supervisor, get_company_name_from_user
from app.models.company import Company
from app.models.customer import Customer
from app.models.division import Division
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_divison import VehicleDivision
from app.models.sale_information import SaleInformation
from app.models.work_shift import WorkShift


def vehicles_list_base_filter(group_by, query, db, current_user, params):
    if check_role_supervisor(current_user):
        company_names = params.get("company_name")
        if company_names is not None:
            query = query.join(Company).filter(
                Customer.company_id == Company.id,
                Company.name.in_(company_names),
            )
    else:
        company_names = get_company_name_from_user(current_user, db)
        query = query.join(Company).filter(
            Customer.company_id == Company.id,
            Company.name.in_(company_names),
        )
    customer_names = params.get("customer_name")
    if customer_names is not None:
        query = query.filter(
            Customer.customer_name.in_(customer_names),
        )
    division_names = params.get("division_name")
    if division_names is not None:
        query = (
            query.join(VehicleDivision)
            .join(Division)
            .filter(
                Vehicle.id == VehicleDivision.vehicle_id,
                Division.id == VehicleDivision.division_id,
                Division.name.in_(division_names),
            )
        )
    work_shifts = params.get("work_shift")
    if work_shifts is not None:
        query = query.join(WorkShift).filter(
            Vehicle.id == WorkShift.vehicle_id,
        )
        work_shift_ids = []
        for item in work_shifts:
            work_shift_id = db.query(WorkShift.id).filter(
                WorkShift.work_shift == item.get("shift"),
                WorkShift.work_shift_from == item.get("ws_from"),
                WorkShift.work_shift_to == item.get("ws_to"),
            )
            data = work_shift_id.all()
            for ws in data:
                work_shift_ids.append(ws[0])
        query = query.filter(WorkShift.id.in_(work_shift_ids))
    model_ids = params.get("model_id")
    if model_ids is not None:
        query = query.filter(Vehicle.model_id.in_(model_ids))
    vehicle_numbers = params.get("vehicle_number")
    if vehicle_numbers is not None:
        query = query.filter(
            Vehicle.vehicle_number.in_(vehicle_numbers),
        )
    operation_status = params.get("operation_status")
    if operation_status is not None:
        query = query.filter(
            Vehicle.operation_status.in_(operation_status),
        )
    sale_id = params.get("sale_id")
    if sale_id is not None:
        query = query.filter(Vehicle.sale_id == sale_id)
    sale_type = params.get("sale_type")
    if sale_type is not None:
        query = query.filter(Vehicle.sale_type == sale_type)
    location = params.get("location")
    if location is not None:
        query = query.filter(Vehicle.location == location)
    forklift_pdi_status = params.get("forklift_pdi_status")
    if forklift_pdi_status is not None:
        query = query.filter(
            Vehicle.forklift_pdi_status == forklift_pdi_status,
        )
    sale_order_number = params.get("sale_order_number")
    if sale_order_number is not None:
        query = query.filter(
            Vehicle.sale_id == sale_order_number,
        )
    if group_by is not None:
        query = query.group_by(group_by)
    return query


def get_vehicle_list(
    filters,
    current_page,
    page_size,
    order_by,
    db,
    current_user,
):
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
    query = vehicles_list_base_filter(
        Vehicle.vehicle_number, query, db, current_user, filters
    )
    total = query.count()
    edges = [i.edge_id for i in query.all()]
    if order_by == "asc":
        query = query.order_by(Vehicle.vehicle_number.asc())
    elif order_by == "customer_name":
        query = query.order_by(Customer.customer_name.asc())
    else:
        query = query.order_by(Vehicle.vehicle_number.desc())
    offset = (current_page - 1) * page_size
    query = query.limit(page_size).offset(offset).all()
    results = {
        "total": total,
        "currentPage": current_page,
        "totalPage": math.ceil(total / page_size),
        "vehicles": jsonable_encoder(query),
        "list_edge": edges,
    }
    return results
