from datetime import timedelta
from unittest import TestCase

from fastapi.testclient import TestClient
from sqlalchemy.orm.session import close_all_sessions

from app.common.database import DBBaseCustom, engine
from app.config.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from app.services.auth import create_access_token
from main import app
from tests.factories.user import UserFactory


def get_user():
    admin_user = UserFactory.create(role_name="SCG-Inter Administrator")
    company_user = UserFactory.create(username="test1", role_name="SCG")
    guest = UserFactory.create(username="test2", role_name="Wrong")
    return admin_user, company_user, guest


def get_token_for_test(username):
    token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)),
    )
    return token


class BaseTestCase(TestCase):
    client = TestClient(app)

    def setUp(self):
        DBBaseCustom.metadata.create_all(bind=engine)
        self.admin_user, self.company_user, self.guest = get_user()
        token = get_token_for_test(self.admin_user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}

    def tearDown(self):
        close_all_sessions()
        DBBaseCustom.metadata.drop_all(engine)
