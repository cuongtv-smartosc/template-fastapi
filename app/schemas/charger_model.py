from pydantic import BaseModel, Field


# Shared properties
class ChargerModelBase(BaseModel):
    name: str = Field(description="The ID that  charger")
    model: str = Field(description="Charger model")


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
