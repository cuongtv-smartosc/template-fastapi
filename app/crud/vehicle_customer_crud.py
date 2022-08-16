from app.crud.base_crud import CRUDBase
from app.models.electric_vehicle_customer import VehicleCustomer
from app.schemas.electric_vehicle_customer import VehicleCustomerCreate


class VehicleCustomerCrud(
    CRUDBase[
        VehicleCustomer,
        VehicleCustomerCreate,
        VehicleCustomerCreate,
    ]
):
    pass


vehicle_customer_crud = VehicleCustomerCrud(VehicleCustomer)