from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.common.database import get_db
from app.crud.user_crud import user_crud
from app.models.user import UserModel
from app.schemas.response import resp
from app.schemas.user import UserCreate
from app.services.auth import get_current_user, get_password_hash

user_router = APIRouter()


@user_router.get("/")
async def get_users(current_user: UserModel = Depends(get_current_user),
                    db: Session = Depends(get_db), ):
    """
        This endpoint get users
    """
    users = await user_crud.list(db=db)
    return users


@user_router.post("/create")
async def create_user(
        user: UserCreate,
        current_user: UserModel = Depends(get_current_user),
        db: Session = Depends(get_db),
):
    """
        This endpoint interacts with the creation of user
    """
    user.hash_password = get_password_hash(user.hash_password)
    await user_crud.create(db=db, obj_in=user)
    return resp.success(data=user)
