from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import Session

from src.db.config_db_sqlalchemy import DBBaseCustom, ActiveSession


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Model"
    name = Column(String, unique=True, index=True, primary_key=True)
    description = Column(String)


class ChargerResponse(BaseModel):
    """This the serializer exposed on the API"""

    name: Optional[str]
    description: Optional[str] = None


class VehicleModelIncoming(BaseModel):
    """This is the serializer used for POST/PATCH requests"""
    name: Optional[str]
    description: Optional[str] = None
