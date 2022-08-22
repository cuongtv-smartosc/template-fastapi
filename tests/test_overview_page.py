from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.charger import ChargerFactory
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory
from tests.factories.vehicle_model import VehicleModelFactory


class TestVehicle(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        CustomerFactory.create()
        SaleInformationFactory.create()
        VehicleModelFactory.create()
        ChargerFactory.create()
        VehicleFactory.create()

    def test_pdi_status_chart(self):
        response = self.client.get(f"{settings.API_PREFIX}/pdi_status_chart")

        res = response.json()
        assert response.status_code == 200
        assert len(res["data"]) == 4
        assert res["msg"] == "success"

    def test_sale_type_stats(self):
        response = self.client.get(f"{settings.API_PREFIX}/sale_type_stats")

        res = response.json()
        assert response.status_code == 200
        assert len(res["data"]) == 4
        assert res["msg"] == "success"
