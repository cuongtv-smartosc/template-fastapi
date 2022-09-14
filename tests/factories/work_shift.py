import factory.fuzzy
from factory import LazyAttribute

from app.common.database import SessionLocal
from app.models.work_shift import WorkShift
from tests.factories.electric_vehicle import VehicleFactory


class WorkShiftFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = WorkShift
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    vehicle_id = LazyAttribute(lambda a: VehicleFactory().id)
