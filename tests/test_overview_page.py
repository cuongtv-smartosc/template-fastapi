from app.common.util import range_time_test_api
from app.config import settings
from tests.base_test import BaseTestCase, get_token_for_test
from tests.factories.company import CompanyFactory
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory

#
from tests.factories.user import UserFactory


class TestSaleTypeStat(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        sale_infor = SaleInformationFactory

        sale_infor.create_batch(
            3,
            sale_type="rent",
        )
        sale_infor.create_batch(
            7,
            sale_type="sold",
        )
        sale_infor.create_batch(
            9,
            sale_type="inventory_used",
        )
        sale_infor.create_batch(
            1,
            sale_type="inventory_new",
        )

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


class TestPdiStatusChart(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        vehicle = VehicleFactory

        vehicle.create_batch(
            5,
            forklift_pdi_status="shipping",
        )
        vehicle.create_batch(
            4,
            forklift_pdi_status="in_warehouse",
        )
        vehicle.create_batch(
            3,
            forklift_pdi_status="assembled",
        )
        vehicle.create_batch(
            2,
            forklift_pdi_status="pdi_completed",
        )
        vehicle.create_batch(
            6,
            forklift_pdi_status="delivered",
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
        assert result["percent"] == [
            25.0,
            20.0,
            15.0,
            10.0,
            0.0,
            30.0,
        ]
        assert len(result) == 4


class TestSaleTypeStatNoData(BaseTestCase):
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
        assert data["datasets"]["values"] == [0, 0, 0, 0]
        assert result["colors"] == [
            "#0072DB",
            "#469BFF",
            "#AAAFC7",
            "#50CC65",
        ]
        assert result["percent"] == [0, 0, 0, 0]
        assert len(result) == 4


class TestPdiStatusChartNoData(BaseTestCase):
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
        assert data["datasets"]["values"] == [0, 0, 0, 0, 0, 0]
        assert result["colors"] == [
            "#469BFF",
            "rgba(70, 155, 255, 0.7)",
            "#AAAFC7",
            "#FFC459",
            "#FC6563",
            "rgba(80, 204, 101, 0.7)",
        ]
        assert result["percent"] == [0, 0, 0, 0, 0, 0]
        assert len(result) == 4


class TestContractExpireReports(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        UserFactory.create()
        token = get_token_for_test(UserFactory.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        sale_infor = SaleInformationFactory
        vehicle = VehicleFactory
        vehicle.create_batch(
            3,
            sale_id=sale_infor(
                sale_order_number="00009",
                end_date=range_time_test_api(44),
            ).id,
        )
        vehicle.create_batch(
            5,
            sale_id=sale_infor(
                sale_order_number="00008",
                end_date=range_time_test_api(45),
            ).id,
        )
        vehicle.create_batch(
            4,
            sale_id=sale_infor(
                sale_order_number="00010",
                end_date=range_time_test_api(395),
            ).id,
        )

    def test_contract_expire_report_desc(self):
        params = {
            "page": 0,
            "number_of_record": 10,
            "expire_period": "0-3 months",
            "sort_by": "remaining_days",
            "sort_order": "desc",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/contract_expire_reports", params=params
        )

        data = response.json().get("data")
        result = data.get("results")
        assert result[0]["contract_number"] == "00008"
        assert result[1]["contract_number"] == "00009"
        assert result[0]["number_of_vehicles"] == 5
        assert result[1]["number_of_vehicles"] == 3
        assert result[0]["remaining_days"] == 45
        assert result[1]["remaining_days"] == 44
        assert result[0]["expire_date"] == range_time_test_api(45)
        assert result[1]["expire_date"] == range_time_test_api(44)
        assert data["summary"]["total_page"] == 1

    def test_contract_expire_report_asc(self):
        params = {
            "page": 1,
            "number_of_record": 1,
            "expire_period": "0-3 months",
            "sort_by": "remaining_days",
            "sort_order": "asc",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/contract_expire_reports", params=params
        )
        data = response.json().get("data")
        result = data.get("results")
        assert result[0]["contract_number"] == "00008"
        assert result[0]["number_of_vehicles"] == 5
        assert result[0]["remaining_days"] == 45
        assert result[0]["expire_date"] == range_time_test_api(45)
        assert data["summary"]["total_page"] == 2

    def test_contract_expire_report_no_filter(self):
        params = {}
        response = self.client.get(
            f"{settings.API_PREFIX}/contract_expire_reports", params=params
        )
        data = response.json().get("data")
        result = data.get("results")
        assert result[0]["contract_number"] == "00009"
        assert result[0]["number_of_vehicles"] == 3
        assert result[0]["remaining_days"] == 44
        assert result[0]["expire_date"] == range_time_test_api(44)
        assert data["summary"]["total_page"] == 1


class TestVehicleByLocations(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        UserFactory.create()
        token = get_token_for_test(UserFactory.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        sale_infor = SaleInformationFactory
        vehicle = VehicleFactory

        vehicle.create_batch(
            3,
            sale_id=sale_infor(location="Ha Noi").id,
        )
        vehicle.create_batch(
            4,
            sale_id=sale_infor(location="Ha Nam").id,
        )
        vehicle.create_batch(
            5,
            sale_id=sale_infor(location="Hai Duong").id,
        )
        vehicle.create_batch(
            6,
            sale_id=sale_infor(location="Hai Phong").id,
        )
        vehicle.create_batch(
            7,
            sale_id=sale_infor(location="Ho Chi Minh").id,
        )
        vehicle.create_batch(
            3,
            sale_id=sale_infor(location="Ha Tay").id,
        )

    def test_vehicle_by_location_desc(self):
        params = {
            "page": 0,
            "number_of_record": 2,
            "sort_by": "number_of_vehicles",
            "sort_order": "desc",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/vehicle_by_locations", params=params
        )

        data = response.json().get("data")
        results = data.get("results")
        summary = data.get("summary")

        assert results[0]["location"] == "Ho Chi Minh"
        assert results[1]["location"] == "Hai Phong"
        assert results[0]["number_of_vehicles"] == 7
        assert results[1]["number_of_vehicles"] == 6
        assert summary["current_page"] == 1
        assert summary["total_page"] == 3

    def test_vehicle_by_location_sort_order_more(self):
        params = {
            "page": 0,
            "number_of_record": 2,
            "sort_by": "number_of_vehicles",
            "sort_order": "asc",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/vehicle_by_locations", params=params
        )
        data = response.json().get("data")
        results = data.get("results")
        summary = data.get("summary")

        assert results[0]["location"] == "Ha Noi"
        assert results[1]["location"] == "Ha Tay"
        assert results[0]["number_of_vehicles"] == 3
        assert results[1]["number_of_vehicles"] == 3
        assert summary["current_page"] == 1
        assert summary["total_page"] == 3

    def test_vehicle_by_location_asc(self):
        params = {
            "page": 0,
            "number_of_record": 2,
            "sort_by": "location",
            "sort_order": "asc",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/vehicle_by_locations", params=params
        )
        data = response.json().get("data")
        results = data.get("results")
        summary = data.get("summary")

        assert results[0]["location"] == "Ha Nam"
        assert results[1]["location"] == "Ha Noi"
        assert results[0]["number_of_vehicles"] == 4
        assert results[1]["number_of_vehicles"] == 3
        assert summary["current_page"] == 1
        assert summary["total_page"] == 3
        assert 1 == 1

    def test_vehicle_by_location_no_filter(self):
        params = {}
        response = self.client.get(
            f"{settings.API_PREFIX}/vehicle_by_locations", params=params
        )

        data = response.json().get("data")
        results = data.get("results")
        summary = data.get("summary")
        assert results[0]["location"] == "Ho Chi Minh"
        assert results[1]["location"] == "Hai Phong"
        assert results[2]["location"] == "Hai Duong"
        assert results[3]["location"] == "Ha Nam"
        assert results[4]["location"] == "Ha Noi"
        assert results[0]["number_of_vehicles"] == 7
        assert results[1]["number_of_vehicles"] == 6
        assert results[2]["number_of_vehicles"] == 5
        assert results[3]["number_of_vehicles"] == 4
        assert results[4]["number_of_vehicles"] == 3
        assert summary["current_page"] == 1
        assert summary["total_page"] == 2


class TestGetTotalNumberOfCustomers(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        user = UserFactory.create(role_name="System Manager")
        global user1
        global user2
        user1 = UserFactory.create(username="test1", role_name="SCG")
        user2 = UserFactory.create(username="test2", role_name="Wrong")
        token = get_token_for_test(user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        customer = CustomerFactory

        customer.create_batch(5)
        customer.create_batch(
            4,
            company_id=CompanyFactory(id="2000").id,
        )
        customer.create_batch(
            3,
            company_id=CompanyFactory(id="1512").id,
            system_user=2,
        )

    def test_with_check_role(self):
        params = {}
        response = self.client.get(
            f"{settings.API_PREFIX}/get_total_overview/total_of_customers",
            params=params,
        )

        data = response.json().get("data")
        assert data["total_of_customers"] == 12

    def test_no_check_role(self):
        token1 = get_token_for_test(user1.username)
        self.client.headers = {"Authorization": f"Bearer {token1}"}

        params = {}
        response = self.client.get(
            f"{settings.API_PREFIX}/get_total_overview/total_of_customers",
            params=params,
        )

        data = response.json().get("data")
        assert data["total_of_customers"] == 3

    def test_no_company(self):
        token2 = get_token_for_test(user2.username)
        self.client.headers = {"Authorization": f"Bearer {token2}"}

        params = {}
        response = self.client.get(
            f"{settings.API_PREFIX}/get_total_overview/total_of_customers",
            params=params,
        )
        data = response.json().get("data")
        assert data["total_of_customers"] == 0
