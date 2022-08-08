from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.user_model import UserModel
from app.schemas.user import UserBase, UserCreate


class UserCrud(CRUDBase[UserBase, UserCreate, UserCreate]):
    async def list(
        self,
        db: Session,
    ) -> list[UserModel]:
        return db.query(UserModel).all()


user_crud = UserCrud(UserModel)
