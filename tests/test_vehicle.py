from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.charger import ChargerFactory
from tests.factories.charger_model import ChargerModelFactory
from tests.factories.customer import CustomerFactory
from tests.factories.division import DivisionFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory
from tests.factories.vehicle_division import VehicleDivisionFactory
from tests.factories.vehicle_model import VehicleModelFactory
from tests.factories.work_shift import WorkShiftFactory


class TestVehicle(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        DivisionFactory.create()
        ChargerModelFactory.create()
        CustomerFactory.create()
        SaleInformationFactory.create()
        VehicleModelFactory.create()
        ChargerFactory.create()
        VehicleFactory.create()
        WorkShiftFactory.create()
        VehicleDivisionFactory.create()

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

    def test_detail(self):
        id = "1"
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{id}",
        )
        res = response.json()
        data = res["data"]
        assert len(data) == 3
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data["Charger"]["id"] == "1"
        assert data["Vehicle"]["id"] == "1"
        assert data["VehicleModel"]["id"] == "M1"

    def test_detail_sale_information(self):
        id = "1"
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{id}/sale_information",
        )
        res = response.json()
        data = res["data"]
        assert len(data) == 15
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data["sale_type"] == "1"
        assert data["remaining_day"] == -236

    def test_detail_charger(self):
        id = "1"
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{id}/charger"
        )
        res = response.json()
        data = res["data"]
        assert len(data) == 3
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data["model"] == "1"

    def test_detail_responsibility(self):
        id = "1"
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{id}/responsibility"
        )
        res = response.json()
        data = res["data"]
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(data) == 2
        assert data["zone"][0]["name"] == "zone A"
        assert data["workShift"][0]["id"] == "Ws1"
