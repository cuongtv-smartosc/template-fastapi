import factory.fuzzy

from app.models.electric_vehicle_model import VehicleModel
from tests.base_test import SessionTest


class VehicleModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleModel
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "M1"
    name = factory.Faker('name')