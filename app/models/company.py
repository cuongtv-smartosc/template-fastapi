from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.common.database import DBBaseCustom


class Company(DBBaseCustom):
    __tablename__ = "company"
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
    name = Column(String(255))