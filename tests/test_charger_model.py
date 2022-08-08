from fastapi.testclient import TestClient

from app.common.database import get_db
from app.config import settings
from main import app
from tests.base_test import BaseTestCase, _get_test_db
from tests.factories.charger_model import ChargerModelFactory

app.dependency_overrides[get_db] = _get_test_db
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
