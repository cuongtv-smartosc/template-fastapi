from app.crud.base_crud import CRUDBase
from app.models.sale_information import SaleInformation
from app.schemas.sale_information import SaleInformationCreate


class SaleInformationCrud(
    CRUDBase[SaleInformation, SaleInformationCreate, SaleInformationCreate]
):
    pass


sale_information_crud = SaleInformationCrud(SaleInformation)
