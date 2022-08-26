import json
import math

from fastapi.encoders import jsonable_encoder

from app.common.util import get_company_name_from_user
from app.models.company import Company
from app.models.customer import Customer
from app.models.division import Division
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_divison import VehicleDivision
from app.models.sale_information import SaleInformation
from app.models.user import User
from app.models.work_shift import WorkShift


def check_role(current_user: User):
    roles = current_user.role_name
    if not roles:
        roles = []
    return (
        "SCG-Inter Administrator" in roles
        or "SCG-Inter Fleet Manager" in roles
        or "System Manager" in roles
    )


def vehicles_list_base_filter(params, group_by, query, db, current_user):
    if params:
        if check_role(current_user):
            params = json.loads(params)
            if "company_name" in params:
                query = query.join(Company).filter(
                    Customer.company_id == Company.id,
                    Company.name.in_(params["company_name"]),
                )
        else:
            company_name = get_company_name_from_user(current_user, db)
            query = query.join(Company).filter(
                Customer.company_id == Company.id,
                Company.name.in_(company_name),
            )

        if "customer_name" in params:
            customer_name = params["customer_name"]
            query = query.filter(
                Customer.customer_name.in_(customer_name),
            )

        if "division_name" in params:
            query = (
                query.join(VehicleDivision)
                .join(Division)
                .filter(
                    Vehicle.id == VehicleDivision.vehicle_id,
                    Division.id == VehicleDivision.division_id,
                    Division.name.in_(params["division_name"]),
                )
            )

        if "work_shift" in params:
            query = query.join(WorkShift).filter(
                Vehicle.id == WorkShift.vehicle_id,
            )
            work_shifts = params["work_shift"]
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
        if "model_id" in params:
            query = query.filter(Vehicle.model_id.in_(params["model_id"]))
        if "vehicle_number" in params:
            query = query.filter(
                Vehicle.vehicle_number.in_(params["vehicle_number"]),
            )
        if "operation_status" in params:
            query = query.filter(
                Vehicle.operation_status.in_(params["operation_status"]),
            )
        if "sale_id" in params:
            query = query.filter(Vehicle.sale_id == params.get("sale_id"))
        if "sale_type" in params:
            query = query.filter(Vehicle.sale_type == params.get("sale_type"))
        if "location" in params:
            query = query.filter(Vehicle.location == params.get("location"))
        if "forklift_pdi_status" in params:
            forklift_pdi_status = params.get("forklift_pdi_status")
            query = query.filter(
                Vehicle.forklift_pdi_status == forklift_pdi_status,
            )
        if "sale_order_number" in params:
            query = query.filter(
                Vehicle.sale_id == params.get("sale_order_number"),
            )
        if group_by is not None:
            query = query.group_by(group_by)
    return query


def get_vehicle_list(
    filter=None,
    pageSize=None,
    currentPage=None,
    order_by=None,
    db=None,
    currentUser=None,
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
    query = vehicles_list_base_filter(
        filters, Vehicle.vehicle_number, query, db, currentUser
    )
    total = query.count()
    edges = [i.edge_id for i in query.all()]
    if order_by == "asc":
        query = query.order_by(Vehicle.vehicle_number.asc())
    elif order_by == "customer_name":
        query = query.orderby(Vehicle.customer_name.asc())
    else:
        query = query.order_by(Vehicle.vehicle_number.desc())
    offset = (int(current_page) - 1) * int(page_size)
    query = query.limit(page_size).offset(offset).all()
    results = {
        "total": total,
        "currentPage": current_page,
        "totalPage": math.ceil(total / page_size),
        "vehicles": jsonable_encoder(query),
        "list_edge": edges,
    }
    return results
