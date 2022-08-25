from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.common.database import DBBaseCustom
from app.models.electric_vehicle import Vehicle


class WorkShift(DBBaseCustom):
    __tablename__ = "work_shift"
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
    vehicle_id = Column(Integer, ForeignKey(Vehicle.id))
    workings_day = Column(String(255))
    work_shift = Column(String(255))
    work_shift_from = Column(String(255))
    work_shift_to = Column(String(255))
