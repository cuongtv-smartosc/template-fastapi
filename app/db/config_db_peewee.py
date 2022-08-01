from contextvars import ContextVar

from peewee import _ConnectionState
from playhouse.pool import PooledMySQLDatabase

from app.config.settings import setting

db_state_default = {
    "closed": None,
    "conn": None,
    "ctx": None,
    "transactions": None,
}
db_state = ContextVar("db_state", default=db_state_default.copy())

env_yml = setting.get_config_env()


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


def connect_db(env_yml):
    db = PooledMySQLDatabase(
        database=env_yml.get("DB_DATABASE"),
        stale_timeout=300,
        user=env_yml.get("DB_USER"),
        host=env_yml.get("DB_HOST"),
        password=str(env_yml.get("DB_PASS")),
        port=int(env_yml.get("DB_POST")),
    )
    return db


db = PooledMySQLDatabase(
    database=env_yml.get("DB_DATABASE"),
    stale_timeout=300,
    user=env_yml.get("DB_USER"),
    host=env_yml.get("DB_HOST"),
    password=str(env_yml.get("DB_PASS")),
    port=int(env_yml.get("DB_POST")),
)

# db = connect_db()
db._state = PeeweeConnectionState()
