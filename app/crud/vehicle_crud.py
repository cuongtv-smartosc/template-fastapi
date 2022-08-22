from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle import Vehicle
from app.models.electric_vehicle_model import VehicleModel
from app.schemas.electric_vehicle import VehicleCreate
from app.schemas.electric_vehicle_model import VehicleModelCreate


class VehicleCrud(
    CRUDBase[
        Vehicle,
        VehicleCreate,
        VehicleCreate,
    ]
):
    pass


vehicle_crud = VehicleCrud(Vehicle)