from sqlalchemy import Column, String, DateTime, Date, Float
from datetime import datetime
from app.common.database import DBBaseCustom


class VehicleModel(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(), )
    description = Column(String(255))
    modified = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(),
                      onupdate=datetime.utcnow(), )
    modified_by = Column(String(255))
    owner = Column(String(255))
    vehicle_number = Column(String(255))
    customer_name = Column(String(255))
    customer_address = Column(String(255))
    sale_type = Column(String(255))
    sale_id = Column(String(255))
    serial_number = Column(String(255))
    model_id = Column(String(255))
    car_condition = Column(String(255))
    forklift_pdi_status = Column(String(255))
    charger_id = Column(String(255))
    import_date = Column(Date)
    manufactoring_date = Column(Date)
    asset_register_date = Column(Date)
    delivering_date = Column(Date)
    sale_order_number = Column(String(255))
    location = Column(String(255))
    coordinates = Column(String)
    edge_id = Column(String(255))
    operating_hours = Column(String(255))
    operating_mileage = Column(String(255))
    working_days = Column(String)
    initial_operating_hours = Column(Float)
    initial_operating_mileage = Column(Float)
    operation_status = Column(String(255))
    mileage_value = Column(String(255))
    hr = Column(String(255))
