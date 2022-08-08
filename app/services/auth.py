from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.common.database import SessionLocal
from app.common.handle_error import UnAuthorizedException
from app.config.settings import ALGORITHM, SECRET_KEY
from app.models.user_model import UserModel
from app.utils.util import verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(user, password: str):
    if not user:
        return False
    if not verify_password(password, user.hash_password):
        return False
    return user


def create_access_token(
    data: dict,
    expires_delta: Union[timedelta, None] = None,
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = UnAuthorizedException(message="Not Authentication")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    db = SessionLocal()
    res = db.query(UserModel).all()
    users = jsonable_encoder(res)
    db.close()
    for user in users:
        if user["username"] == username:
            return user
