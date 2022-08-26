from app.crud.base_crud import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate


class UserCrud(CRUDBase[User, UserCreate, UserCreate]):
    pass


user_crud = UserCrud(User)
