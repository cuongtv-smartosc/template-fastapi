from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate


class UserCrud(CRUDBase[User, UserCreate, UserCreate]):
    async def get_by_username(
        self,
        db: Session,
        username: str,
    ):
        return db.query(User).filter(User.username == username).first()


user_crud = UserCrud(User)
