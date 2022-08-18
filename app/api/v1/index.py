from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.schemas.response import resp

router_index = APIRouter()


@router_index.get("/")
async def index(db: Session = Depends(get_db)):
    a = analytic_base_query(db)
    print(a)
    print(type(a))
    for i in a:
        print(i.__dict__)
    return resp.success(data=a)
