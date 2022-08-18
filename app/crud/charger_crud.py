from app.crud.base_crud import CRUDBase
from app.models.charger import Charger
from app.schemas.charger import ChargerCreate


class ChargerCrud(CRUDBase[Charger, ChargerCreate, ChargerCreate]):
    pass


charger_crud = ChargerCrud(Charger)
