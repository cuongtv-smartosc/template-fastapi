from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.charger import ChargerFactory
from tests.factories.charger_model import ChargerModelFactory
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory
from tests.factories.vehicle_model import VehicleModelFactory


class TestVehicle(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        ChargerModelFactory.create()
        CustomerFactory.create()
        SaleInformationFactory.create()
        VehicleModelFactory.create()
        ChargerFactory.create()
        VehicleFactory.create()

    def test_list(self):
        params = {
            "currentPage": 1,
            "order_by": "asc",
            "pageSize": 18,
            "filter": {"offset": "0", "period": "Today"},
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )

        res = response.json()
        data = res["data"]
        assert response.status_code == 200
        assert len(data) == 5
        assert res["msg"] == "success"
        assert data["total"] == 1
        assert data["currentPage"] == "1"
        assert data["totalPage"] == 1
        assert len(data["list_edge"]) == 1
        assert data["vehicles"][0]["id"] == "1"
