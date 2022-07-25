from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestChargerModel:

    def test_list(self):
        response = client.get("/charger-models")
        res = response.json()
        assert response.status_code == 200
        assert res["msg"] == "success"
