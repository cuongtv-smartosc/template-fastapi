from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.common.database import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Division"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(), )
    description = Column(String(255))
    modified = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(),
                      onupdate=datetime.utcnow(), )
    modified_by = Column(String(255))
    owner = Column(String(255))
    id = Column(String(255))
    vehicle_number = Column(String(255))
    vehicle_division = Column(String(255))