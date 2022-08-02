from sqlalchemy import Column, String

from app.db.config_db_sqlalchemy import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Model"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    description = Column(String(255))
