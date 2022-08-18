from pydantic import BaseModel


# Shared properties
class DivisionBase(BaseModel):
    id: str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None
    id: str = None
    division_name: str = None


# Properties to receive on item creation
class DivisionCreate(DivisionBase):
    pass


# Properties to return to client
class DivisionResponse(DivisionBase):
    """This the serializer exposed on the API"""

    pass
