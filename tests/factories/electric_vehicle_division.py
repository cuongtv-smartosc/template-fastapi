import factory.fuzzy

from app.common.database import SessionLocal
from app.models.electric_vehicle_divison import VehicleDivision


class VehicleDivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleDivision
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"
