from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.common.database import SessionLocal, get_db, db_session
from app.models.electric_vehicle import Vehicle
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


def analytic_base_query(db):
    electric_vehicle = VehicleBase
    customer = VehicleCusTomerBase
    division = DivisionBase
    work_shift = WorkShiftBase

    s = select(Vehicle)
    a = db.scalars(s)
    return a
