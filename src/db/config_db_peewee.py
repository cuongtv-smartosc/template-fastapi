from peewee import _ConnectionState
from contextvars import ContextVar
from playhouse.pool import PooledMySQLDatabase

import settings

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = PooledMySQLDatabase(
    settings.DB_NAME,
    stale_timeout=300,
    user=settings.DB_USER,
    host=settings.DB_HOST,
    password=settings.DB_PASS,
    port=int(settings.DB_POST)
)

db._state = PeeweeConnectionState()
