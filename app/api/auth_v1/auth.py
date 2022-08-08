from datetime import timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.handle_error import UnAuthorizedException
from app.config.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from app.crud.user_model_crud import user_crud
from app.schemas.response import resp
from app.schemas.user import Token, UserLogin
from app.services.auth import authenticate_user, create_access_token

auth_jwt = APIRouter()


ACCESS_TOKEN_EXPIRE = int(ACCESS_TOKEN_EXPIRE_MINUTES)


@auth_jwt.post("/login", response_model=Token)
async def login(data: UserLogin, db: Session = Depends(get_db)):
    credentials_exception = UnAuthorizedException(message="Not Authentication")
    user_data = await user_crud.get(db, data.username)
    user = authenticate_user(user_data, data.password)
    if not user:
        raise credentials_exception
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    data = {"access_token": access_token, "token_type": "bearer"}
    return resp.success(data=data)
