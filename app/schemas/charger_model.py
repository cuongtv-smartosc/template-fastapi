from typing import Optional

from pydantic import BaseModel


# Shared properties
class ChargerModelBase(BaseModel):
    name: str = None
    description: Optional[str] = None


# Properties to receive on item creation
class ChargerModelCreate(ChargerModelBase):
    pass


# Properties to return to client
class ChargerModel(ChargerModelBase):
    pass
