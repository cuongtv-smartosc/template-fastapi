from tests.base_test import BaseTestCase, get_token_for_test
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.sale_information import SaleInformationFactory


class GetSaleInformationTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()

        customer = CustomerFactory.create(customer_name="abc", system_user="2")
        sale_if = SaleInformationFactory.create(customer_id=customer.id)
        VehicleFactory.create_batch(3, sale_id=sale_if.id)
        VehicleFactory.create_batch(25)

    def test_get_sale_information_success(self):
        vehicle_id = 1
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("customer_name") == "abc"

    def test_get_sale_information_validate_id_is_int(self):
        vehicle_id = "abc"
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert data[0].get("msg") == "value is not a valid integer"
        assert data[0].get("loc")[0] == "path"
        assert data[0].get("loc")[1] == "id"
        assert data[0].get("type") == "type_error.integer"

    def test_get_sale_information_not_found(self):
        vehicle_id = 29
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"

    def test_get_information_by_user_company_not_found(self):
        vehicle_id = 5
        token = get_token_for_test(username=self.user1.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"

    def test_get_sale_information_by_user_company_success(self):
        vehicle_id = 3
        token = get_token_for_test(username=self.user1.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("customer_name") == "abc"
