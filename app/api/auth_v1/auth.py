from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.config.settings import setting
from app.crud.user_model_crud import user_crud
from app.schemas.response import resp
from app.schemas.user import Token, UserLogin
from app.services.auth import authenticate_user, create_access_token

auth_jwt = APIRouter()
env_yml = setting.get_config_env()
ACCESS_TOKEN_EXPIRE_MINUTES = env_yml.get("ACCESS_TOKEN_EXPIRES_IN")


@auth_jwt.post("/login", response_model=Token)
async def login(data: UserLogin, db: Session = Depends(get_db)):
    user_data = await user_crud.get(db, data.username)
    print(user_data)
    user = authenticate_user(user_data, data.password)
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
    data = {"access_token": access_token, "token_type": "bearer"}
    return resp.success(data=data)
