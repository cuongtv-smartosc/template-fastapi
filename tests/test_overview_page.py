from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.company import CompanyFactory
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory


class TestVehicle(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        CompanyFactory.create()
        CustomerFactory.create()
        SaleInformationFactory.create()
        VehicleFactory.create()

    def test_pdi_status_chart(self):
        response = self.client.get(f"{settings.API_PREFIX}/pdi_status_chart")

        res = response.json()
        res = res["data"]
        data = res["data"]
        assert response.status_code == 200
        assert len(res) == 4
        assert data["labels"] == [
            "Shipping",
            "In Warehouse",
            "Assembled",
            "PDI completed",
            "Asset in inventory",
            "Delivered",
        ]
        assert res["type"] == "pie"
        assert res["colors"] == [
            "#469BFF",
            "rgba(70, 155, 255, 0.7)",
            "#AAAFC7",
            "#FFC459",
            "#FC6563",
            "rgba(80, 204, 101, 0.7)",
        ]
        assert data["datasets"][0]["values"] == [0, 0, 0, 1, 0, 0]
        assert res["percent"] == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0]

    def test_sale_type_stats(self):
        response = self.client.get(f"{settings.API_PREFIX}/sale_type_stats")

        res = response.json()
        res = res["data"]
        data = res["data"]
        assert res["type"] == "pie"
        assert data["labels"] == [
            "Rent",
            "Sold",
            "Inventory (Used)",
            "Inventory (New)",
        ]
        assert res["colors"] == ["#0072DB", "#469BFF", "#AAAFC7", "#50CC65"]
        assert data["datasets"][0]["values"] == [0, 0, 0, 1]
        assert res["percent"] == [0.0, 0.0, 0.0, 100.0]
        assert response.status_code == 200
        assert len(res) == 4
