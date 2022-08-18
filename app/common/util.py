from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.common.database import SessionLocal, get_db, db_session
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_customer import VehicleCustomer
from app.models.electric_vehicle_division import VehicleDivision
from app.models.electric_vehicle_work_shift import VehicleWorkShift
from app.schemas.electric_vehicle import VehicleBase
from app.schemas.electric_vehicle_customer import VehicleCusTomerBase
from app.schemas.electric_vehicle_division import DivisionBase
from app.schemas.electric_vehicle_work_shift import WorkShiftBase


def validate_unique(table, field, **kwargs):
    session = SessionLocal()
    q = session.query(getattr(table, field)).filter_by(**kwargs).scalar()
    session.close()
    if q:
        raise ValueError(f"""Table {table.__name__} {field} already exist""")
    return kwargs[field]


def vehicles_list_base_filter(params, group_by, query):
    if 'company_name' in params:
        company_name = params['company_name']
        query = query.where(VehicleCustomer.company_name.isin(company_name))

    if 'customer_name' in params:
        query = query.where(Vehicle.customer_name.isin(params['customer_name']))

    if 'division_name' in params:
        query = query.inner_join(VehicleDivision).on(Vehicle.vehicle_number == VehicleDivision.vehicle_number).where(
            VehicleDivision.vehicle_division.isin(params['division_name']))

    if 'work_shift' in params:
        query = query.inner_join(VehicleWorkShift).on(Vehicle.name == VehicleWorkShift.vehicle_number)
        work_shifts = params["work_shift"]
        work_shift_names = []
        for item in work_shifts:
            work_shift_name = VehicleWorkShift.query(VehicleWorkShift.name).filter(VehicleWorkShift.work_shift == item.get("shift"),
                                                                       VehicleWorkShift.work_shift_from == item.get(
                                                                           "ws_from"),
                                                                       VehicleWorkShift.work_shift_to == item.get(
                                                                           "ws_to")).all()
            data = work_shift_name.run(as_list=True)
            for ws in data:
                work_shift_names.append(ws[0])
        query = query.where(VehicleWorkShift.name.isin(work_shift_names))

    if 'model_id' in params:
        query = query.where(Vehicle.model_id.isin(params['model_id']))

    if 'vehicle_number' in params:
        query = query.where(
            Vehicle.vehicle_number.isin(params['vehicle_number']))

    if 'operation_status' in params:
        query = query.where(Vehicle.operation_status.isin(
            params['operation_status']))

    if 'sale_id' in params:
        query = query.where(Vehicle.sale_id == params.get('sale_id'))

    if 'sale_type' in params:
        query = query.where(Vehicle.sale_type == params.get('sale_type'))

    if 'location' in params:
        query = query.where(Vehicle.location == params.get('location'))

    if "forklift_pdi_status" in params:
        query = query.where(Vehicle.forklift_pdi_status == params.get('forklift_pdi_status'))

    if "sale_order_number" in params:
        query = query.where(Vehicle.sale_id == params.get('sale_order_number'))

    if group_by is not None:
        query = query.group_by(group_by)

    return query
