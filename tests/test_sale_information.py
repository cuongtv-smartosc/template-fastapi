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
        token = get_token_for_test(username=self.company_user.username)
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
        token = get_token_for_test(username=self.company_user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert data.get("customer_name") == "abc"


class UpdateSaleInformationTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        customer = CustomerFactory.create(customer_name="abc", system_user="2")
        sale_if = SaleInformationFactory.create(
            customer_id=customer.id, sale_order_number="1"
        )
        VehicleFactory.create_batch(3, sale_id=sale_if.id)
        VehicleFactory.create_batch(10)

    def test_update_sale_information_success(self):
        vehicle_id = 1
        body = {
            "id": 1,
            "sale_type": "Rent",
            "sale_order_number": 2,
            "customer_id": 1,
            "customer_name": "test2",
            "address": "BangKok",
            "location": None,
            "delivering_date": "2022-11-22",
            "vehicle_warranty": 1,
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01-01",
            "end_date": "2022-01-01",
            "remaining_day": -257,
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert message == "success"
        assert response.status_code == 200

    def test_update_sale_information_validate_unique_customer_name(self):
        vehicle_id = 4
        body = {
            "id": 2,
            "sale_type": "Rent",
            "sale_order_number": 123122,
            "customer_id": 2,
            "customer_name": "abc",
            "address": "BangKok",
            "location": None,
            "delivering_date": "2022-11-22",
            "vehicle_warranty": 1,
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01-01",
            "end_date": "2022-01-01",
            "remaining_day": -257,
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert message[0].get("loc")[0] == "customer_name"
        assert message[0].get("msg") == "value customer_name is existed"
        assert message[0].get("type") == "value_error"

    def test_update_sale_information_validate_unique_sale_order_number(self):
        vehicle_id = 4
        body = {
            "id": 2,
            "sale_type": "Rent",
            "sale_order_number": 1,
            "customer_id": 2,
            "customer_name": "abc",
            "address": "BangKok",
            "location": None,
            "delivering_date": "2022-11-22",
            "vehicle_warranty": 1,
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01-01",
            "end_date": "2022-01-01",
            "remaining_day": -257,
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert message[0].get("loc")[0] == "sale_order_number"
        assert message[0].get("msg") == "value sale_order_number is existed"
        assert message[0].get("type") == "value_error"

    def test_update_sale_information_validate_vehicle_warranty_is_int(self):
        vehicle_id = 1
        body = {
            "id": 1,
            "sale_type": "Rent",
            "sale_order_number": 2,
            "customer_id": 1,
            "customer_name": "test2",
            "address": "BangKok",
            "location": None,
            "delivering_date": "2022-11-22",
            "vehicle_warranty": "a",
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01-01",
            "end_date": "2022-01-01",
            "remaining_day": -257,
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert message[0].get("loc")[0] == "body"
        assert message[0].get("loc")[1] == "vehicle_warranty"
        assert message[0].get("msg") == "value is not a valid integer"
        assert message[0].get("type") == "type_error.integer"

    def test_update_sale_information_validate_start_date_is_date(self):
        vehicle_id = 1
        body = {
            "id": 1,
            "sale_type": "Rent",
            "sale_order_number": 2,
            "customer_id": 1,
            "customer_name": "test2",
            "address": "BangKok",
            "location": None,
            "delivering_date": "2022-11-22",
            "vehicle_warranty": 1,
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01",
            "end_date": "2022-01-01",
            "remaining_day": -257,
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert message[0].get("loc")[0] == "start_date"
        assert message[0].get("msg") == "invalid date format"
        assert message[0].get("type") == "value_error"

    def test_update_sale_information_validate_delivering_date_is_date(self):
        vehicle_id = 1
        body = {
            "id": 1,
            "sale_type": "Rent",
            "sale_order_number": 2,
            "customer_id": 1,
            "customer_name": "test2",
            "address": "BangKok",
            "location": None,
            "delivering_date": "a",
            "vehicle_warranty": 1,
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01-01",
            "end_date": "2022-01-01",
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert message[0].get("loc")[0] == "delivering_date"
        assert message[0].get("msg") == "invalid date format"
        assert message[0].get("type") == "value_error"

    def test_update_sale_information_validate_end_date_is_date(self):
        vehicle_id = 1
        body = {
            "id": 1,
            "sale_type": "Rent",
            "sale_order_number": 2,
            "customer_id": 1,
            "customer_name": "test2",
            "address": "BangKok",
            "location": None,
            "delivering_date": None,
            "vehicle_warranty": 1,
            "battery_warranty": None,
            "battery_maintenance": None,
            "service": None,
            "start_date": "2021-01-01",
            "end_date": "2022",
        }
        response = self.client.patch(
            f"/api/electric_vehicle/{vehicle_id}/sale_information",
            json=body,
        )
        res = response.json()
        message = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 422
        assert message[0].get("loc")[0] == "end_date"
        assert message[0].get("msg") == "invalid date format"
        assert message[0].get("type") == "value_error"
