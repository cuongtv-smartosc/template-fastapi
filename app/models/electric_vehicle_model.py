from sqlalchemy import Column, String

from app.db.config_db_sqlalchemy import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Model"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(String(255))
    description = Column(String(255))
    modified = Column(String(255))
    modified_by = Column(String(255))
    owner = Column(String(255))
    model = Column(String(255))
