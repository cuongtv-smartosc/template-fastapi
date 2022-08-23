import factory.fuzzy

from app.models.electric_vehicle_divison import VehicleDivision
from tests.base_test import SessionTest


class VehicleDivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleDivision
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "div1"
    division_id = "zoneA"
    vehicle_id = "1"
