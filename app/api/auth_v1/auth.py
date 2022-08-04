from datetime import timedelta
from fastapi import APIRouter, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer

from app.models.user_model import users_db
from app.schemas.response import resp
from app.schemas.user import UserLogin, Token
from app.config.settings import setting
from app.services.auth import authenticate_user, create_access_token


auth_jwt = APIRouter()
env_yml = setting.get_config_env()
ACCESS_TOKEN_EXPIRE_MINUTES = env_yml.get("ACCESS_TOKEN_EXPIRES_IN")


@auth_jwt.post("/login", response_model=Token)
async def login(data: UserLogin, response: Response):
    user = authenticate_user(users_db, data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie('access_token', access_token, ACCESS_TOKEN_EXPIRE_MINUTES*60,
                        ACCESS_TOKEN_EXPIRE_MINUTES*60, '/', None, False, True, 'lax')
    response.set_cookie('logged_in', 'True', ACCESS_TOKEN_EXPIRE_MINUTES*60,
                        ACCESS_TOKEN_EXPIRE_MINUTES*60, '/', None, False, False, 'lax')
    data = {"access_token": access_token, "token_type": "bearer"}
    return data