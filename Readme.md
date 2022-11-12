
# Using Python 3.9.13 64 Bits Windows Store

## create env: 
python -m venv ./venv/

## open env:
.\venv\Scripts\activate

## Dependencies:
- pip install uvicorn fastapi
- pip install sqlalchemy
- pip install psycopg2

## Select Venv python version in VS COde

## Run API
### inside app folder:
uvicorn main:app --reload