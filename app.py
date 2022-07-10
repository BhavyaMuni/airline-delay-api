from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from typing import List

import database.models as models, database.schemas as schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/{carrier}-{flight}", response_model=schemas.Record)
def show_records(carrier: str, flight:int, db: Session = Depends(get_db)):
    records = db.query(models.Record).filter(models.Record.unique_carrier == carrier and models.Record.flight_num == flight).first()
    print(db.query(models.Record).filter(models.Record.unique_carrier == carrier and models.Record.flight_num == flight).count())
    return records