from sqlalchemy import Column, Integer, String, Float, true
from database.database import Base

class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(Integer)
    day_of_month= Column(Integer)
    day_of_week= Column(Integer)
    dep_time= Column(Float)
    crs_dep_time= Column(Integer)
    arr_time= Column(Float)
    crs_arr_time= Column(Integer)
    unique_carrier= Column(String, index=True)
    flight_num= Column(Integer, index=True)
    tail_num= Column(String)
    actual_elapsed_time= Column(Float)
    crs_elapsed_time= Column(Float)
    air_time= Column(Float)
    arr_delay= Column(Float)
    dep_delay= Column(Float)
    origin= Column(String)
    dest= Column(String)
    distance= Column(Integer)
    taxi_in= Column(Float)
    taxi_out= Column(Float)
    cancelled= Column(Integer)
    cancellation_code= Column(String)
    carrier_delay= Column(Float)
    weather_delay= Column(Float)
    nas_delay= Column(Float)
    security_delay= Column(Float)
    late_aircraft_delay= Column(Float)
