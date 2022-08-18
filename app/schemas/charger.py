from pydantic import BaseModel
from app.common.util import validate_unique
from app.models.charger_model import ChargerModel


# Shared properties
class ChargerBase(BaseModel):
    id: str = None
    description: None | str = None
    modified_by: str = None
    owner: str = None


# Properties to receive on item creation
class ChargerCreate(ChargerBase):
    pass


# Properties to return to client
class ChargerResponse(ChargerBase):
    """This the serializer exposed on the API"""

    pass
