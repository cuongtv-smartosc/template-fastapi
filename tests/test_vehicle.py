from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.charger import ChargerFactory
from tests.factories.charger_model import ChargerModelFactory
from tests.factories.company import CompanyFactory
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory
from tests.factories.vehicle_model import VehicleModelFactory


class TestVehicle(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        companies = CompanyFactory.create_batch(10)
        customers = CustomerFactory.create_batch(
            10,
            company_id=companies[0].id,
        )
        sale_if = SaleInformationFactory.create_batch(
            30,
            customer_id=customers[1].id,
        )
        charger_models = ChargerModelFactory.create_batch(30)
        chargers = ChargerFactory.create_batch(
            30,
            model=charger_models[1].id,
        )
        vehicle_models = VehicleModelFactory.create_batch(
            30,
        )
        VehicleFactory.create_batch(
            30,
            sale_id=sale_if[10].id,
            model_id=vehicle_models[2].id,
            charger_id=chargers[3].id,
        )

    def test_list(self):
        params = {
            "currentPage": 1,
            "order_by": "asc",
            "pageSize": 10,
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
        assert data["total"] == 30
        assert data["currentPage"] == "1"
        assert data["totalPage"] == 3
