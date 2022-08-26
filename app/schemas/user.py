from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    username: str = None
    hash_password: str = None


class UserCreate(UserBase):

    pass


class UserResponse(UserBase):
    """This the serializer exposed on the API"""

    pass
