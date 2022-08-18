from sqlalchemy import Column, String, DateTime, Date, Float, Integer
from datetime import datetime

from sqlalchemy.orm import relationship

from app.common.database import DBBaseCustom


class VehicleSaleInformation(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Sale Information"
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
    customer_id = Column(String(255))
    sale_order_number = Column(String(255))
    sale_type = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    vehicle_warranty = Column(Integer)
    battery_warranty = Column(Integer)
    battery_maintenance = Column(Integer)
    location = Column(String(255))
    service = Column(String(255))
    product_number = Column(String(255))
    coordinates = Column(String(255))
    working_days = Column(String(255))
    electric_vehicle = relationship('Vehicle', backref='tabElectric Vehicle Sale Information')