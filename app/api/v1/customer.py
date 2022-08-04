from pydantic import BaseModel, Field
from fastapi.routing import APIRouter
from fastapi import status

app = APIRouter()


class ElectricCustomer(BaseModel):
    id: int = Field(description="The ID that the customer uses to login everywhere")
    age: int = Field(description="The official age of the customer")
    gender: str = Field(default=None, description="The gender of the customer, if they wan to disclose it",
                        max_length=8)


@app.post("/customers", response_model=ElectricCustomer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: ElectricCustomer):
    return customer
