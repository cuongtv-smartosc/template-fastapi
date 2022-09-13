from tests.base_test import BaseTestCase, get_token_for_test
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.electric_vehicle_history import VehicleHistoryFactory
from tests.factories.sale_information import SaleInformationFactory
from tests.factories.user import UserFactory


class GetStatusTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        user = UserFactory.create()
        global user2
        user2 = UserFactory.create(username="guest", role_name="")
        token = get_token_for_test(username=user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        customer = CustomerFactory.create(customer_name="abc", system_user="2")
        sale_if = SaleInformationFactory.create(customer_id=customer.id)
        VehicleFactory.create_batch(2, sale_id=sale_if.id)
        VehicleHistoryFactory.create_batch(6)
        VehicleHistoryFactory.create_batch(4, vehicle_id=1, status="offline")
        VehicleHistoryFactory.create_batch(4, vehicle_id=1, status="online")
        VehicleHistoryFactory.create_batch(4, vehicle_id=1, status="spare")
        VehicleHistoryFactory.create_batch(2, vehicle_id=2)

    def test_get_status_success(self):
        vehicle_id = 1
        params = {
            "current_page": "1",
            "page_size": "10",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("total") == 12
        assert data.get("currentPage") == 1
        assert data.get("totalPage") == 2
        assert len(data.get("data")) == 10

    def test_get_status_by_current_page(self):
        vehicle_id = 1
        params = {
            "current_page": "2",
            "page_size": "10",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("total") == 12
        assert data.get("currentPage") == 2
        assert data.get("totalPage") == 2
        assert len(data.get("data")) == 2

    def test_get_status_by_filters(self):
        vehicle_id = 1
        params = {"current_page": "1", "page_size": "10", "status": "online"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("total") == 4
        assert data.get("currentPage") == 1
        assert data.get("totalPage") == 1
        assert len(data.get("data")) == 4

    def test_get_status_validate_page_size_is_int(self):
        vehicle_id = 1
        params = {
            "current_page": "1",
            "page_size": "asdasd",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert data[0].get("msg") == "value is not a valid integer"
        assert data[0].get("loc")[0] == "query"
        assert data[0].get("loc")[1] == "page_size"
        assert data[0].get("type") == "type_error.integer"

    def test_get_status_validate_current_page_is_int(self):
        vehicle_id = 1
        params = {
            "current_page": "error",
            "page_size": "12",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert data[0].get("msg") == "value is not a valid integer"
        assert data[0].get("loc")[0] == "query"
        assert data[0].get("loc")[1] == "current_page"
        assert data[0].get("type") == "type_error.integer"

    def test_get_status_validate_current_page_is_ge_1(self):
        vehicle_id = 1
        params = {
            "current_page": "-1",
            "page_size": "12",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        msg = data[0].get("msg")
        assert msg == "ensure this value is greater than or equal to 1"
        assert data[0].get("loc")[0] == "query"
        assert data[0].get("loc")[1] == "current_page"
        assert data[0].get("type") == "value_error.number.not_ge"

    def test_get_status_by_current_page_than_total_page(self):
        vehicle_id = 1
        params = {
            "current_page": "100",
            "page_size": "12",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert data.get("data") == []

    def test_get_status_not_found_vehicle(self):
        vehicle_id = 20
        params = {
            "current_page": "1",
            "page_size": "10",
        }
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"

    def test_get_status_by_user_company_success(self):
        vehicle_id = 2
        params = {
            "current_page": "1",
            "page_size": "10",
        }
        token = get_token_for_test(username=user2.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("total") == 2
        assert data.get("currentPage") == 1
        assert data.get("totalPage") == 1
        assert len(data.get("data")) == 2

    def test_get_status_by_user_company_not_found_vehicle(self):
        vehicle_id = 3
        params = {
            "current_page": "1",
            "page_size": "10",
        }
        token = get_token_for_test(username=user2.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/status", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"
