import factory.fuzzy

from app.common.database import SessionLocal
from app.models.electric_vehicle_model import VehicleModel


class VehicleModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleModel
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    name = factory.fuzzy.FuzzyText("id")
