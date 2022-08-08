from unittest import TestCase

from app.common.database import DBBaseCustom, SessionLocal, engine


class BaseTestCase(TestCase):
    def setUp(self):
        DBBaseCustom.metadata.create_all(bind=engine)

    def tearDown(self):
        SessionLocal().close()
        DBBaseCustom.metadata.drop_all(engine)
