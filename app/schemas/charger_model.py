from pydantic import BaseModel, constr, validator

from app.common.database import SessionLocal
from app.models.charger_model import ChargerModel


class ChargerModelBase(BaseModel):
    name: constr(min_length=3, max_length=20, strip_whitespace=True)
    owner: constr(min_length=1, max_length=20)


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    @validator("name")
    def check(self, v):
        session = SessionLocal()
        q = session.query(ChargerModel.name).filter_by(name=v).scalar()
        session.close()
        if q:
            raise ValueError("Model name already exist")
        return v


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
