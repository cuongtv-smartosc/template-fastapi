from app.crud.base_crud import CRUDBase
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate


class CustomerCrud(CRUDBase[Customer, CustomerCreate, CustomerCreate]):
    pass


customer_crud = CustomerCrud(Customer)
