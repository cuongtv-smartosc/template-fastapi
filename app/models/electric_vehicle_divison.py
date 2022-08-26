from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.common.database import DBBaseCustom


class VehicleDivision(DBBaseCustom):
    __tablename__ = "vehicle_division"
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
    vehicle_id = Column(Integer, ForeignKey("electric_vehicle.id"))
    division_id = Column(Integer, ForeignKey("division.id"))
