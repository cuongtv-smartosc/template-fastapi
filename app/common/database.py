import sys

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.config.settings import setting

if "pytest" in sys.modules:
    setting.env = "local_test"
env_yml = setting.get_config_env()
engine = create_engine(env_yml.get("DB_URL"))

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBBaseCustom = declarative_base()


def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


ActiveSession = Depends(get_db)
