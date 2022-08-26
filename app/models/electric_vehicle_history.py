from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.common.database import DBBaseCustom


class VehicleHistory(DBBaseCustom):
    __tablename__ = "vehicle_history"
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
    status = Column(String(255))
    detail = Column(String(255))
    update_by = Column(String(255))
    update_time = Column(DateTime)
    vehicle_id = Column(
        Integer,
        ForeignKey("electric_vehicle.id"),
    )
    create_time = Column(DateTime)
    amended_from = Column(String(255))
    islatest = Column(Integer)
