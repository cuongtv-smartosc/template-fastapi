from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.common.database import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "vehicle_model"
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
    description = Column(String(255))
    owner = Column(String(255))
    name = Column(String(255))
    # vehicle = relationship('Vehicle', backref='vehicle_model', lazy=False)
