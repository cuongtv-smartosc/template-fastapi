import factory.fuzzy
from factory import LazyAttribute

from app.common.database import SessionLocal
from app.models.electric_vehicle import Vehicle
from tests.factories.charger import ChargerFactory
from tests.factories.electric_vehicle_model import VehicleModelFactory
from tests.factories.sale_information import SaleInformationFactory


class VehicleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Vehicle
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    edge_id = factory.fuzzy.FuzzyText("edge_id")
    vehicle_number = factory.fuzzy.FuzzyText("vehicle_number")
    sale_id = LazyAttribute(lambda a: SaleInformationFactory().id)

    forklift_pdi_status = factory.fuzzy.FuzzyChoice(
        [
            "shipping",
            "in_warehouse",
            "assembled",
            "pdi_completed",
            "asset_in_inventory",
            "delivered",
        ]
    )
    charger_id = LazyAttribute(lambda a: ChargerFactory().id)
    model_id = LazyAttribute(lambda a: VehicleModelFactory().id)
