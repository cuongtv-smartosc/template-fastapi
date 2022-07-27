from peewee import _ConnectionState
from contextvars import ContextVar
from playhouse.pool import PooledMySQLDatabase

from settings import EnvDB

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
    EnvDB.DB_NAME,
    stale_timeout=300,
    user=EnvDB.DB_USER,
    host=EnvDB.DB_HOST,
    password=EnvDB.DB_PASS,
    port=int(EnvDB.DB_POST)
)

db._state = PeeweeConnectionState()
