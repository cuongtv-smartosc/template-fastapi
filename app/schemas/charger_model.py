from pydantic import Field, constr, validator

from app.common.util import validate_unique
from app.models.charger_model import ChargerModel
from app.schemas.base import BaseModelSchemas


class ChargerModelBase(BaseModelSchemas):
    id: constr(min_length=3, max_length=20, strip_whitespace=True) = Field(
        description="The ID that  charger"
    )
    name: str = Field(description="Charger model")


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    @validator("id")
    def unique_check_model(cls, v):
        return validate_unique(ChargerModel, "id", name=v)


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
