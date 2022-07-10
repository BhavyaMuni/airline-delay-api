import csv
import datetime

from database import models
from database.database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("good_data.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = models.Record(
            id=int(row[""]),
            month=int(row["Month"]),
            day_of_month=int(row["DayofMonth"]),
            day_of_week=int(row["DayOfWeek"]),
            dep_time=float(row["DepTime"]),
            crs_dep_time=int(row["CRSDepTime"]),
            arr_time=float(row["ArrTime"]),
            crs_arr_time=int(row["CRSArrTime"]),
            unique_carrier=row["UniqueCarrier"],
            flight_num=int(row["FlightNum"]),
            tail_num=row["TailNum"],
            actual_elapsed_time=float(row["ActualElapsedTime"]),
            crs_elapsed_time=float(row["CRSElapsedTime"]),
            air_time=float(row["AirTime"]),
            arr_delay=float(row["ArrDelay"]),
            dep_delay=float(row["DepDelay"]),
            origin=row["Origin"],
            dest=row["Dest"],
            distance=int(row["Distance"]),
            taxi_in=float(row["TaxiIn"]),
            taxi_out=float(row["TaxiOut"]),
            cancelled=int(row["Cancelled"]),
            cancellation_code=row["CancellationCode"],
            carrier_delay=float(row["CarrierDelay"]),
            weather_delay=float(row["WeatherDelay"]),
            nas_delay=float(row["NASDelay"]),
            security_delay=float(row["SecurityDelay"]),
            late_aircraft_delay=float(row["LateAircraftDelay"]),
        )
        db.add(db_record)

    db.commit()

db.close()