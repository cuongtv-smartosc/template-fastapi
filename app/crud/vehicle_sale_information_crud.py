from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle_sale_information import VehicleSaleInformation
from app.schemas.sale_information import SaleInformationCreate


class VehicleSaleInformationCrud(
    CRUDBase[
        VehicleSaleInformation,
        SaleInformationCreate,
        SaleInformationCreate,
    ]
):
    pass


vehicle_sale_information_crud = VehicleSaleInformationCrud(VehicleSaleInformation)