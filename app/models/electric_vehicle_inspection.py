from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from app.common.database import DBBaseCustom


class VehicleInspection(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Inspection"
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
    no = Column(String(255))
    status = Column(String(255))
    detail = Column(String(255))
    update_by = Column(String(255))
    update_time = Column(DateTime)
    ev_number = Column(String(255))
    create_time = Column(DateTime)
    amended_from = Column(String(255))
    islatest = Column(Integer)
