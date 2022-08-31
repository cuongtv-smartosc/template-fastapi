import factory.fuzzy

from app.models.electric_vehicle_history import VehicleHistory
from tests.base_test import SessionTest


class VehicleHistoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleHistory
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"
