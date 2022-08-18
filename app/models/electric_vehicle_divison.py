from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from app.common.database import DBBaseCustom
from app.models.division import Division
from app.models.electric_vehicle import Vehicle


class VehicleDivision(DBBaseCustom):
    __tablename__ = "vehicle_division"
    id = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(), )
    modified = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(),
                      onupdate=datetime.utcnow(), )
    modified_by = Column(String(255))
    owner = Column(String(255))
    vehicle_id = Column(String(255), ForeignKey(Vehicle.id))
    division_id = Column(String(255), ForeignKey(Division.id))