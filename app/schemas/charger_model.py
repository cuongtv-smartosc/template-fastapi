from pydantic import BaseModel


# Shared properties
class ChargerModelBase(BaseModel):
    name: str = None
    description: None | str = None


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
