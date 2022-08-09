from sqlalchemy import Column, String

from app.common.database import DBBaseCustom


class ChargerModel(DBBaseCustom):
    __tablename__ = "tabCharger Model"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    model = Column(String(255))
    creation = Column(String(255))
    modified = Column(String(255))
