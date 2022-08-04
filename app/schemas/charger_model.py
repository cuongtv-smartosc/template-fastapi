from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, conint, constr, validator

from app.db.config_db_sqlalchemy import SessionLocal
from app.models.charger_model import ChargerModel


class ChargerModelBase(BaseModel):
    name: constr(
        min_length=3, max_length=20, strip_whitespace=True
    )  # curtail_length=10
    description: conint(ge=2, le=10, multiple_of=2)  # gt, ge, lt, le


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    @validator("name")
    def name_must_contain_space(cls, v):
        if " " in v:
            raise ValueError("Not contain a space")
        return v

    # @validator("description")
    # def description_format(cls, v):
    #     if not v.isalnum():
    #         raise ValueError("Must be alphanumeric")
    #     return v
    @validator("name")
    def check(cls, v):
        session = SessionLocal()
        res = session.query(ChargerModel).all()
        data = jsonable_encoder(res)
        md_name = [data[item].get("name", None) for item in range(len(data))]
        if v in md_name:
            raise ValueError("Model name already exist")
        return v


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
