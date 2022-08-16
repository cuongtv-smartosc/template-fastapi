from sqlalchemy import Column, String, DateTime, Date, Float
from datetime import datetime
from app.common.database import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Customer"
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
    customer_name = Column(String(255))
    address = Column(String(255))
    company_name = Column(String(255))
    system_user = Column(String(255))