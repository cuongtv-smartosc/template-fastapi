from pydantic import BaseModel
from pydantic.schema import datetime


class BaseModelSchemas(BaseModel):
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


class BaseModelUpdate(BaseModel):
    modified: datetime = None
    modified_by: str = None
