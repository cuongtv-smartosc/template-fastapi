import factory.fuzzy
from factory import LazyAttribute

from app.common.database import SessionLocal
from app.models.electric_vehicle_divison import VehicleDivision
from tests.factories.division import DivisionFactory
from tests.factories.electric_vehicle import VehicleFactory


class VehicleDivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleDivision
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    vehicle_id = LazyAttribute(lambda a: VehicleFactory().id)
    division_id = LazyAttribute(lambda a: DivisionFactory().id)
