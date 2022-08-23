import factory.fuzzy

from app.models.electric_vehicle import Vehicle
from tests.base_test import SessionTest


class VehicleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Vehicle
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "1"
    edge_id = factory.fuzzy.FuzzyText("edge_id")
    vehicle_number = factory.fuzzy.FuzzyText("vehicle_number")
    sale_id = "S1"
    charger_id = "1"
    model_id = "M1"
