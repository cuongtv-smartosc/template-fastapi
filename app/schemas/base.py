from pydantic import BaseModel


class BaseModelSchemas(BaseModel):
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None