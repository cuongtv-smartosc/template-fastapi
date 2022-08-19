from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, String, Integer
from app.common.database import DBBaseCustom
from app.models.division import Division
from app.models.electric_vehicle import Vehicle


class VehicleHistory(DBBaseCustom):
    __tablename__ = "vehicle_history"
    id = Column(String(255), unique=True, index=True, primary_key=True)
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
    vehicle_id = Column(String(255), ForeignKey(Vehicle.id))
    create_time = Column(DateTime)
    amended_from = Column(String(255))
    islatest = Column(Integer)
