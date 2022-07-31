# from typing import Optional
#
# from pydantic import BaseModel
# from sqlalchemy import Column, String
#
# from src.db.config_db_sqlalchemy import DBBaseCustom
#
#
# class VehicleModel(DBBaseCustom):
#     __tablename__ = "tabElectric Vehicle Model"
#     name = Column(String(255), unique=True, index=True, primary_key=True)
#     description = Column(String(255))
#
#
# class ChargerResponse(BaseModel):
#     """This the serializer exposed on the API"""
#
#     name: Optional[str]
#     description: Optional[str] = None
#
#
# class VehicleModelIncoming(BaseModel):
#     """This is the serializer used for POST/PATCH requests"""
#     name: Optional[str]
#     description: Optional[str] = None
