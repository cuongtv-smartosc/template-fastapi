from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle_company import VehicleCompany
from app.schemas.electric_vehicle_company import VehicleCompanyCreate


class VehicleCompanyCrud(
    CRUDBase[
        VehicleCompany,
        VehicleCompanyCreate,
        VehicleCompanyCreate,
    ]
):
    pass


vehicle_company_crud = VehicleCompanyCrud(VehicleCompany)