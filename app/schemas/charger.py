from pydantic import BaseModel, Field, constr, validator

from app.common.util import validate_unique
from app.models.charger_model import ChargerModel


# Shared properties
class ChargerBase(BaseModel):
    name: str = None
    description: None | str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


# Properties to receive on item creation
class ChargerCreate(ChargerBase):
    pass


# Properties to return to client
class ChargerResponse(ChargerBase):
    """This the serializer exposed on the API"""

    pass
