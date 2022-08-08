from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import close_all_sessions

from app.common.database import DBBaseCustom
from app.config.settings import setting

setting.env = "local_test"
env_yml = setting.get_config_env()
engine_test = create_engine(env_yml.get("DB_URL"))
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def _get_test_db():
    try:
        yield SessionTest()
    finally:
        pass


class BaseTestCase(TestCase):
    def setUp(self):
        DBBaseCustom.metadata.create_all(bind=engine_test)

    def tearDown(self):
        close_all_sessions()
        DBBaseCustom.metadata.drop_all(engine_test)
