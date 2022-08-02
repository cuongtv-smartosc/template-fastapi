from pydantic import BaseModel, validator


# Shared properties
class ChargerModelBase(BaseModel):
    name: str = None
    model: None | str = None

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("Must contain a space")
        return v.title()

    @validator("description")
    def description_format(cls, v):
        if not v.isalnum():
            raise ValueError("Must be alphanumeric")
        return v


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


# Properties to return to client
class ChargerModelResponse(ChargerModelBase):
    """This the serializer exposed on the API"""

    pass
