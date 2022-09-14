from app.config import settings
from tests.base_test import BaseTestCase, get_token_for_test
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory

integer_validate_error = "value is not a valid integer"


class GetVehiclesTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()

        customer = CustomerFactory.create(customer_name="abc")
        sale_if = SaleInformationFactory.create(customer_id=customer.id)
        VehicleFactory.create_batch(3, sale_id=sale_if.id)
        VehicleFactory.create_batch(25)

    def test_get_vehicles_success(self):
        params = {
            "current_page": 1,
            "page_size": 10,
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("data")
        vehicles = data.get("vehicles")
        list_edge = data.get("list_edge")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(vehicles) == 10
        assert data.get("total") == 28
        assert len(list_edge) == 28

    def test_get_vehicles_by_current_page(self):
        params = {
            "current_page": 3,
            "page_size": 10,
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("data")
        vehicles = data.get("vehicles")
        list_edge = data.get("list_edge")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(vehicles) == 8
        assert data.get("total") == 28
        assert len(list_edge) == 28

    def test_get_vehicles_by_page_size(self):
        params = {
            "current_page": 1,
            "page_size": 18,
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("data")
        vehicles = data.get("vehicles")
        list_edge = data.get("list_edge")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(vehicles) == 18
        assert data.get("total") == 28
        assert len(list_edge) == 28

    def test_get_list_by_customer_name(self):
        params = {
            "current_page": "1",
            "page_size": "18",
            "customer_name": '["abc"]',
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("data")
        vehicles = data.get("vehicles")
        list_edge = data.get("list_edge")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(vehicles) == 3
        assert data.get("total") == 3
        assert len(list_edge) == 3

    def test_get_list_by_error_page_size(self):
        params = {
            "current_page": "1",
            "page_size": "error",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert data[0].get("msg") == integer_validate_error

    def test_get_list_by_error_customer_name(self):
        params = {
            "current_page": "1",
            "page_size": "10",
            "customer_name": "asdasd",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code == 422
        assert data[0].get("msg") == "value is not a valid list"
        assert data[0].get("type") == "value_error"

    def test_get_list_by_error_current_page(self):
        params = {
            "current_page": "asdasd",
            "page_size": "10",
        }
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle", params=params
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert data[0].get("msg") == integer_validate_error
        assert data[0].get("loc")[1] == "current_page"


class GetVehicleDetailTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()

        customer = CustomerFactory.create(system_user="2")
        sale_if = SaleInformationFactory.create(customer_id=customer.id)
        VehicleFactory.create_batch(3, sale_id=sale_if.id)
        VehicleFactory.create_batch(25)

    def test_get_detail_success(self):
        vehicle_id = 1
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{vehicle_id}",
        )
        res = response.json()
        data = res.get("data")
        detail = data.get("detail")
        charger = data.get("detail")
        model = data.get("model")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert detail.get("id") == 1
        assert detail.get("charger_id") == charger.get("id")
        assert detail.get("model_id") == model.get("id")

    def test_get_detail_validate_id_is_int(self):
        vehicle_id = "abc"
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{vehicle_id}",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert data[0].get("msg") == integer_validate_error
        assert data[0].get("loc")[0] == "path"
        assert data[0].get("loc")[1] == "id"
        assert data[0].get("type") == "type_error.integer"

    def test_get_detail_not_found(self):
        vehicle_id = 29
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{vehicle_id}",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"

    def test_get_detail_by_user_company_success(self):
        token = get_token_for_test(username=self.company_user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        vehicle_id = 3
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{vehicle_id}",
        )
        res = response.json()
        data = res.get("data")
        detail = data.get("detail")
        charger = data.get("detail")
        model = data.get("model")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert detail.get("id") == 3
        assert detail.get("charger_id") == charger.get("id")
        assert detail.get("model_id") == model.get("id")

    def test_get_detail_by_user_company_not_found(self):
        token = get_token_for_test(username=self.company_user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        vehicle_id = 4
        response = self.client.get(
            f"{settings.API_PREFIX}/electric_vehicle/{vehicle_id}",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"
