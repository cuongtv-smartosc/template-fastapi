from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.common.database import SessionLocal
from app.common.handle_error import UnAuthorizedException
from app.config.settings import ALGORITHM, SECRET_KEY
from app.models.user import UserModel
from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
        this function is used for hashing password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
        this function is used for verifying hash password with request password
    """
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


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
    """
        this function is used for creating access token as jwt token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
        This function is used for getting authenticated user.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UnAuthorizedException()
    except JWTError:
        raise UnAuthorizedException()
    db = SessionLocal()
    res = db.query(UserModel).all()
    users = jsonable_encoder(res)
    db.close()
    for user in users:
        if user["username"] == username:
            return user
