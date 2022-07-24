# AIRLINES DELAY API

## Trying out FastAPI for Python. Used with SQlLITE local database. This is a testing project not a complete app.

## Usage

1. Download Kaggle dataset to root folder
   `https://www.kaggle.com/datasets/giovamata/airlinedelaycauses`
2. Run all the cells from `data.ipynb`
   - this will generate file `good_data.csv`
3. Run `load_database.py` to populate the database
4. App is ready to run using `uvicorn app:app`

### Accomplished

- Fast API for basic CRUD operations
- Connection to a local database
- SQL querying and filtering the database
- Aggregate functions in SQLAlchemy
