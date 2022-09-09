from datetime import timedelta
from unittest import TestCase

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import close_all_sessions

from app.common.database import DBBaseCustom, get_db
from app.config.settings import ACCESS_TOKEN_EXPIRE_MINUTES, setting
from app.services.auth import create_access_token
from main import app

setting.env = "local_test"
env_yml = setting.get_config_env()
engine_test = create_engine(env_yml.get("DB_URL"))
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def _get_test_db():
    try:
        yield SessionTest()
    finally:
        pass


def get_token_for_test(username):
    token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)),
    )
    return token


class BaseTestCase(TestCase):
    app.dependency_overrides[get_db] = _get_test_db
    client = TestClient(app)

    def setUp(self):
        DBBaseCustom.metadata.create_all(bind=engine_test)

    def tearDown(self):
        close_all_sessions()
        DBBaseCustom.metadata.drop_all(engine_test)
