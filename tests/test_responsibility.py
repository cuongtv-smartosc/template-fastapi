from tests.base_test import BaseTestCase, get_token_for_test
from tests.factories.customer import CustomerFactory
from tests.factories.electric_vehicle import VehicleFactory
from tests.factories.electric_vehicle_division import VehicleDivisionFactory
from tests.factories.sale_information import SaleInformationFactory
from tests.factories.work_shift import WorkShiftFactory


class GetResponsibilityTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        customer = CustomerFactory.create(customer_name="abc", system_user="2")
        sale_if = SaleInformationFactory.create(customer_id=customer.id)
        VehicleFactory.create_batch(2, sale_id=sale_if.id)
        VehicleDivisionFactory.create_batch(4)
        VehicleDivisionFactory.create_batch(4, vehicle_id=1)
        VehicleDivisionFactory.create_batch(4, vehicle_id=2)
        WorkShiftFactory.create_batch(4)
        WorkShiftFactory.create_batch(4, vehicle_id=1)

    def test_get_responsibility_success(self):
        vehicle_id = 1
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/responsibility",
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(data.get("zone")) == 4
        assert len(data.get("workShift")) == 4

    def test_get_responsibility_not_found_vehicle(self):
        vehicle_id = 11
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/responsibility",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"

    def test_get_responsibility_by_user_company_success(self):
        token = get_token_for_test(username=self.company_user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        vehicle_id = 2
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/responsibility",
        )
        res = response.json()
        data = res.get("data")
        assert response.status_code == 200
        assert res["msg"] == "success"
        assert len(data.get("zone")) == 4
        assert len(data.get("workShift")) == 0

    def test_get_responsibility_by_user_company_not_found_vehicle(self):
        vehicle_id = 3
        token = get_token_for_test(username=self.company_user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get(
            f"/api/electric_vehicle/{vehicle_id}/responsibility",
        )
        res = response.json()
        data = res.get("message")
        assert response.status_code != 200
        assert response.status_code == 404
        assert data == f"{vehicle_id} is not existed"
