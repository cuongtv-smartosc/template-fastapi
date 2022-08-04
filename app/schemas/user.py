from typing import Union, Optional, List
from pydantic import BaseModel, Field, validator

users_db = {
    "linh": {
        "username": "linh",
        "full_name": "Linh Vu",
        "hashed_password": "1",
    },
    "mai": {
        "username": "mai",
        "full_name": "Huyen Mai",
        "hashed_password": "2",
    },
}


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


class UserInDB(User):
    hash_password: str