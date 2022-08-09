from sqlalchemy.orm import Session
from app.crud.base_crud import CRUDBase
from app.models.user import UserModel
from app.schemas.user import UserBase, UserCreate


class UserCrud(CRUDBase[UserBase, UserCreate, UserCreate]):
    async def list_by_owner(
            self,
            db: Session,
            owner: str,
    ) -> list[UserModel]:
        return db.query(UserModel).filter(UserModel.owner == owner).all()


user_crud = UserCrud(UserModel)
