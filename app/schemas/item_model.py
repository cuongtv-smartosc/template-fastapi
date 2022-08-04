from typing import List, Union, Generic, TypeVar, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

class Error(BaseModel):
    code: int
    message: str

# Shared properties
class ItemModel(BaseModel):
    name: str
    #name: str = Field(alias='name_')
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []
