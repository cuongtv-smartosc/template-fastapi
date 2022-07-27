from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

from settings import EnvDB

engine = create_engine(
    EnvDB.DB_URL
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBBaseCustom = declarative_base()


def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = Session()
        yield db
    finally:
        db.close()


ActiveSession = Depends(get_db)


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
