from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.charger_model import ChargerModel
from app.schemas.charger_model import ChargerModelCreate


class ChargerModelCrud(
    CRUDBase[
        ChargerModel,
        ChargerModelCreate,
        ChargerModelCreate,
    ]
):
    async def list_by_owner(
        self,
        db: Session,
        owner: str,
    ) -> list[ChargerModel]:
        return db.query(ChargerModel).filter(ChargerModel.owner == owner).all()


charger_model_crud = ChargerModelCrud(ChargerModel)
