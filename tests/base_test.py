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
    user = UserFactory.create(role_name="SCG-Inter Administrator")
    user1 = UserFactory.create(username="test1", role_name="SCG")
    user2 = UserFactory.create(username="test2", role_name="Wrong")
    return user, user1, user2


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
        self.user, self.user1, self.user2 = get_user()
        token = get_token_for_test(self.user.username)
        self.client.headers = {"Authorization": f"Bearer {token}"}

    def tearDown(self):
        close_all_sessions()
        DBBaseCustom.metadata.drop_all(engine)
