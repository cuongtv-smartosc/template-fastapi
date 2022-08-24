from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.company import CompanyFactory
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory


class TestVehicle(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        company = CompanyFactory
        customer = CustomerFactory
        sale_infor = SaleInformationFactory
        vehicle = VehicleFactory
        company.create_batch(33, id=company.id)

        customer.create_batch(
            33,
            id=customer.id,
            customer_name=customer.customer_name,
            company_id=company.id,
        )
        sale_infor.create_batch(
            33,
            id=sale_infor.id,
            sale_type=sale_infor.sale_type,
            sale_order_number=sale_infor.sale_order_number,
            end_date=sale_infor.end_date,
            customer_id=customer.id,
        )
        vehicle.create_batch(
            33,
            id=vehicle.id,
            edge_id=vehicle.edge_id,
            vehicle_number=vehicle.vehicle_number,
            sale_id=sale_infor.id,
            forklift_pdi_status=vehicle.forklift_pdi_status,
        )

    def test_pdi_status_chart(self):
        response = self.client.get(f"{settings.API_PREFIX}/pdi_status_chart")

        res = response.json()
        res = res["data"]
        data = res["data"]
        assert response.status_code == 200
        assert res["type"] == "pie"
        assert data["labels"] == [
            "Shipping",
            "In Warehouse",
            "Assembled",
            "PDI completed",
            "Asset in inventory",
            "Delivered",
        ]
        assert data["datasets"]["values"] == [6, 6, 6, 5, 5, 5]
        assert res["colors"] == [
            "#0072DB",
            "#469BFF",
            "#AAAFC7",
            "#50CC65",
        ]
        assert res["percent"] == [
            18.181818181818183,
            18.181818181818183,
            18.181818181818183,
            15.151515151515152,
            15.151515151515152,
            15.151515151515152,
        ]
        assert len(res) == 4
