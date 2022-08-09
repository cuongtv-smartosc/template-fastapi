from pydantic import BaseModel, Field, constr, validator

from app.common.database import SessionLocal
from app.models.charger_model import ChargerModel


# Shared properties
class ChargerModelBase(BaseModel):
    name: constr(min_length=3, max_length=20, strip_whitespace=True) = Field(
        description="The ID that  charger"
    )
    model: str = Field(description="Charger model")


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    @validator("name")
    def unique_check_name(self, v):
        session = SessionLocal()
        q = session.query(ChargerModel.name).filter_by(name=v).scalar()
        session.close()
        if q:
            raise ValueError("Model name already exist")
        return v

    @validator("model")
    def unique_check_model(self, v):
        session = SessionLocal()
        q = session.query(ChargerModel.model).filter_by(model=v).scalar()
        session.close()
        if q:
            raise ValueError("Model already exist")
        return v


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
