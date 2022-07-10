from lib2to3.pytree import Base
from pydantic import BaseModel

class Record(BaseModel):
    id: int
    month : int
    day_of_month: int
    day_of_week: int
    dep_time: float
    crs_dep_time: int
    arr_time: float
    crs_arr_time: int
    unique_carrier: str
    flight_num: int
    tail_num: str
    actual_elapsed_time: float
    crs_elapsed_time: float
    air_time: float
    arr_delay: float
    dep_delay: float
    origin: str
    dest: str
    distance: int
    taxi_in: float
    taxi_out: float
    cancelled: int
    cancellation_code: str
    carrier_delay: float
    weather_delay: float
    nas_delay: float
    security_delay: float
    late_aircraft_delay: float

    class Config():
        orm_mode = True