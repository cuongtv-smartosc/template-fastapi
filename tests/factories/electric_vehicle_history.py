import random

import factory.fuzzy
from factory import LazyAttribute

from app.models.electric_vehicle_history import VehicleHistory
from tests.base_test import SessionTest
from tests.factories.electric_vehicle import VehicleFactory


class VehicleHistoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = VehicleHistory
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    status = factory.fuzzy.FuzzyChoice(
        ["online", "offline", "spare"],
    )
    vehicle_id = LazyAttribute(lambda a: VehicleFactory().id)
    update_time = (
        f"2022-{random.randint(1, 12)}-{random.randint(1, 28)} 15:03:40.000",
    )
