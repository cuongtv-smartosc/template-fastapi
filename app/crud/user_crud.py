from sqlalchemy.orm import Session
from app.crud.base_crud import CRUDBase
from app.models.user import UserModel
from app.schemas.user import UserBase, UserCreate


class UserCrud(CRUDBase[UserBase, UserCreate, UserCreate]):
    pass


user_crud = UserCrud(UserModel)
