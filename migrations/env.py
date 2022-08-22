import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine

from app.common.database import DBBaseCustom
from app.config.settings import setting
from app.models import (
    charger,
    charger_model,
    company,
    customer,
    division,
    electric_vehicle,
    electric_vehicle_divison,
    electric_vehicle_history,
    electric_vehicle_model,
    sale_information,
    user,
    work_shift,
)

charger = charger
charger_model = charger_model
company = company
customer = customer
division = division
electric_vehicle = electric_vehicle
electric_vehicle_divison = electric_vehicle_divison
electric_vehicle_history = electric_vehicle_history
electric_vehicle_model = electric_vehicle_model
sale_information = sale_information
user = user
work_shift = work_shift
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = DBBaseCustom.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    env_yml = setting.get_config_env()
    url = env_yml.get("DB_URL_Alembic")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    env_yml = setting.get_config_env()
    url = env_yml.get("DB_URL_Alembic")
    engine = create_engine(url)
    connectable = AsyncEngine(engine)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
