import random

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

        companys = company.create_batch(20)
        ran = random.choice(companys).id
        customers = customer.create_batch(
            20, customer_name=customer.customer_name, company_id=ran
        )
        sale_infors = sale_infor.create_batch(
            3,
            sale_type="rent",
            sale_order_number=sale_infor.sale_order_number,
            end_date=sale_infor.end_date,
            customer_id=customers[0].id,
        )
        sale_infor.create_batch(
            7,
            sale_type="sold",
            sale_order_number=sale_infor.sale_order_number,
            end_date=sale_infor.end_date,
            customer_id=customers[0].id,
        )
        sale_infor.create_batch(
            9,
            sale_type="inventory_used",
            sale_order_number=sale_infor.sale_order_number,
            end_date=sale_infor.end_date,
            customer_id=customers[0].id,
        )
        sale_infor.create_batch(
            1,
            sale_type="inventory_new",
            sale_order_number=sale_infor.sale_order_number,
            end_date=sale_infor.end_date,
            customer_id=customers[0].id,
        )
        vehicle.create_batch(
            5,
            edge_id=vehicle.edge_id,
            vehicle_number=vehicle.vehicle_number,
            forklift_pdi_status="shipping",
            sale_id=sale_infors[0].id,
        )
        vehicle.create_batch(
            4,
            edge_id=vehicle.edge_id,
            vehicle_number=vehicle.vehicle_number,
            forklift_pdi_status="in_warehouse",
            sale_id=sale_infors[0].id,
        )
        vehicle.create_batch(
            3,
            edge_id=vehicle.edge_id,
            vehicle_number=vehicle.vehicle_number,
            forklift_pdi_status="assembled",
            sale_id=sale_infors[0].id,
        )
        vehicle.create_batch(
            2,
            edge_id=vehicle.edge_id,
            vehicle_number=vehicle.vehicle_number,
            forklift_pdi_status="pdi_completed",
            sale_id=sale_infors[0].id,
        )
        vehicle.create_batch(
            6,
            edge_id=vehicle.edge_id,
            vehicle_number=vehicle.vehicle_number,
            forklift_pdi_status="delivered",
            sale_id=sale_infors[0].id,
        )

    def test_pdi_status_chart(self):
        response = self.client.get(f"{settings.API_PREFIX}/pdi_status_charts")

        result = response.json().get("data")
        data = result.get("data")
        assert response.status_code == 200
        assert result["type"] == "pie"
        assert data["labels"] == [
            "Shipping",
            "In Warehouse",
            "Assembled",
            "PDI completed",
            "Asset in inventory",
            "Delivered",
        ]
        assert data["datasets"]["values"] == [5, 4, 3, 2, 0, 6]
        assert result["colors"] == [
            "#469BFF",
            "rgba(70, 155, 255, 0.7)",
            "#AAAFC7",
            "#FFC459",
            "#FC6563",
            "rgba(80, 204, 101, 0.7)",
        ]
        assert result["percent"] == [25.0, 20.0, 15.0, 10.0, 0.0, 30.0]
        assert len(result) == 4

    def test_sale_type_stat(self):
        response = self.client.get(f"{settings.API_PREFIX}/sale_type_stats")

        result = response.json().get("data")
        data = result.get("data")
        assert response.status_code == 200
        assert result["type"] == "pie"
        assert data["labels"] == [
            "Rent",
            "Sold",
            "Inventory (Used)",
            "Inventory (New)",
        ]
        assert data["datasets"]["values"] == [3, 7, 9, 1]
        assert result["colors"] == [
            "#0072DB",
            "#469BFF",
            "#AAAFC7",
            "#50CC65",
        ]
        assert result["percent"] == [15.0, 35.0, 45.0, 5.0]
        assert len(result) == 4
