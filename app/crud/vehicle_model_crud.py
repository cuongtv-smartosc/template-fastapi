from typing import List

from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle_model import VehicleModel
from app.schemas.electric_vehicle_model import VehicleModelCreate


class VehicleModelCrud(
    CRUDBase[
        VehicleModel,
        VehicleModelCreate,
        VehicleModelCreate,
    ]
):
    async def list_by_owner(
        self,
        db: Session,
        owner: str,
    ) -> List[VehicleModel]:
        return db.query(VehicleModel).filter(VehicleModel.owner == owner).all()


vehicle_model_crud = VehicleModelCrud(VehicleModel)
