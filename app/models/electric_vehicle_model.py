from datetime import datetime

from sqlalchemy import DECIMAL, Column, DateTime, Integer, String

from app.common.database import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Model"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime, nullable=False, default=datetime.utcnow())
    description = Column(String(255))
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))
    model = Column(String(255))
    wheel_diameter = Column(String(255))
    max_voltage = Column(String(255))
    wheel_diameter_inch = Column(DECIMAL(21, 9))
    wheel_diameter_meter = Column(DECIMAL(21, 9))
    speed = Column(String(255))
    direction = Column(String(255))
    belt_alert_value = Column(String(255))
    smart_belt = Column(String(255))
    battery_capacity = Column(Integer(11))
    battery_current = Column(Integer(11))
    can_battery_scale = Column(Integer(11))
