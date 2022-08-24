import factory.fuzzy

from app.models.electric_vehicle import Vehicle
from tests.base_test import SessionTest


class VehicleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Vehicle
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: "114-%04d" % n)
    edge_id = factory.fuzzy.FuzzyText("edge_id")
    vehicle_number = factory.fuzzy.FuzzyText("vehicle_number")
    sale_id = factory.Sequence(lambda n: "113-%04d" % n)
    forklift_pdi_status = factory.Iterator(
        [
            "shipping",
            "in_warehouse",
            "assembled",
            "pdi_completed",
            "asset_in_inventory",
            "delivered",
        ]
    )
