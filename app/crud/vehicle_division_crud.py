from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle_division import VehicleDivision
from app.schemas.electric_vehicle_division import DivisionCreate


class VehicleDivisionCrud(
    CRUDBase[
        VehicleDivision,
        DivisionCreate,
        DivisionCreate,
    ]
):
    pass


vehicle_division_crud = VehicleDivisionCrud(VehicleDivision)