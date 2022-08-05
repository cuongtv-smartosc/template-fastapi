from fastapi.testclient import TestClient

from app.config import settings
from main import app
from tests.base_test import BaseTestCase
from tests.factories.charger_model import ChargerModelFactory

client = TestClient(app)


class TestChargerModel(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        ChargerModelFactory.create()

    def test_list(self):
        response = client.get(f"{settings.API_PREFIX}/charger-models")
        res = response.json()
        assert response.status_code == 200
        assert len(res["data"]) == 1
        assert res["msg"] == "success"
