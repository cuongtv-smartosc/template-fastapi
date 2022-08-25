from sqlalchemy import Column, Integer, String

from app.common.database import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "vehicle_model"
    id = Column(
        Integer,
        unique=True,
        index=True,
        primary_key=True,
        autoincrement=True,
    )
    creation = Column(String(255))
    description = Column(String(255))
    modified = Column(String(255))
    modified_by = Column(String(255))
    owner = Column(String(255))
    name = Column(String(255))
