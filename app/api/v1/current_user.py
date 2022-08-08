from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.crud.user_model_crud import user_crud
from app.models.user_model import UserModel
from app.schemas.response import resp
from app.schemas.user import UserCreate
from app.services.auth import get_current_user

user = APIRouter()


@user.get("/")
async def get_current_user(
    current_user: UserModel = Depends(get_current_user),
):
    return current_user


@user.post("/create")
async def create_user(
    User: UserCreate,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    await user_crud.create(db=db, obj_in=User)
    return resp.success(data=User)
