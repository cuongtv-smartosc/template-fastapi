from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Float
from sqlalchemy import ForeignKey as FK
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from app.common.database import DBBaseCustom


class Vehicle(DBBaseCustom):
    __tablename__ = "electric_vehicle"
    id = Column(
        Integer,
        unique=True,
        index=True,
        primary_key=True,
        autoincrement=True,
    )
    creation = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))
    vehicle_number = Column(String(255))
    serial_number = Column(String(255))
    model_id = Column(Integer, FK("vehicle_model.id"))
    car_condition = Column(String(255))
    forklift_pdi_status = Column(String(255))
    import_date = Column(Date)
    asset_register_date = Column(Date)
    delivering_date = Column(Date)
    edge_id = Column(String(255))
    operating_hours = Column(String(255))
    operating_mileage = Column(String(255))
    initial_operating_hours = Column(Float, default=0.000000000)
    initial_operating_mileage = Column(Float, default=0.000000000)
    operation_status = Column(String(255))
    mileage_value = Column(String(255))
    hr = Column(String(255))
    sale_id = Column(Integer, FK("sale_information.id"))
    charger_id = Column(Integer, FK("charger.id"))
    electric_division = relationship(
        "VehicleDivision",
        backref="electric_vehicle",
    )
    work_shift = relationship("WorkShift", backref="electric_vehicle")
