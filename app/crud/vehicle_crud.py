from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle import Vehicle
from app.schemas.electric_vehicle import VehicleCreate


class VehicleCrud(
    CRUDBase[
        Vehicle,
        VehicleCreate,
        VehicleCreate,
    ]
):
    pass


vehicle_crud = VehicleCrud(Vehicle)