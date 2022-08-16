from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle_work_shift import VehicleWorkShift
from app.schemas.work_shift import WorkShiftCreate


class VehicleWorkShiftCrud(
    CRUDBase[
        VehicleWorkShift,
        WorkShiftCreate,
        WorkShiftCreate,
    ]
):
    pass


vehicle_work_shift_crud = VehicleWorkShiftCrud(VehicleWorkShift)