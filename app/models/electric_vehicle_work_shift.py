from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.common.database import DBBaseCustom


class VehicleWorkShift(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Work Shift"
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
    vehicle_number = Column(String(255))
    workings_day = Column(String(255))
    work_shift = Column(String(255))
    work_shift_from = Column(String(255))
    work_shift_to = Column(String(255))
