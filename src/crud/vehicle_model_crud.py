from typing import List

from sqlalchemy.orm import Session

from src.crud.base_crud import CRUDBase
# from src.models.electric_vehicle_model import VehicleModelIncoming, VehicleModel

#
# class VehicleModelCrud(CRUDBase[VehicleModel, VehicleModelIncoming, VehicleModelIncoming]):
#
#     async def list_by_owner(self, db: Session, owner: str) -> List[VehicleModel]:
#         return db.query(VehicleModel).filter(VehicleModel.owner == owner).all()
#
#
# vehicle_model_crud = VehicleModelCrud(VehicleModel)
