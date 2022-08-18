from datetime import datetime
from sqlalchemy import Column, DateTime, String
from app.common.database import DBBaseCustom


class ChargerModel(DBBaseCustom):
    __tablename__ = "charger model"
    id = Column(String(255), unique=True, index=True, primary_key=True)
    model = Column(String(255))
    creation = Column(DateTime, nullable=False, default=datetime.utcnow())
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))