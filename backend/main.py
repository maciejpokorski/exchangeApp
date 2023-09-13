from fastapi import FastAPI
from datetime import datetime
from typing import List
from task import setup_daily_task
from cors import setup_cors
from database.config import setup_db
from db_service import DBService
from utils import fetch_remote_data

app = FastAPI()

# init
setup_cors(app)
db_service = DBService()
setup_daily_task(app)

@app.get("/fetch_remote_data/{date}")
async def fetch_data(date: str):
    # validate input date
    try:
        if datetime.strptime(date, "%Y-%m-%d") >= datetime.now():
            return {"error": "Date parameter must be in the past"}
    except ValueError:
        return {"error": "Date parameter must be valid and in YYYY-MM-DD format"}
    
    try:
        enabled_currencies = [c.code for c in db_service.get_enabled_currencies()]
        data = await fetch_remote_data(date)
        return get_rates_for_given_currencies(data, enabled_currencies)
    except Exception as e:
        return {"error": f"Request error: {e}"}

@app.get("/fetch_local_data/")
async def fetch_local_data():
    enabled_currencies = [c.code for c in db_service.get_enabled_currencies()]
    data = db_service.get_exchange_rates()
    result = []
    for item in data:
        exchange_rate = {
            "Date": item.date,
        }
        exchange_rate.update(get_rates_for_given_currencies(item.rates, enabled_currencies))
        result.append(exchange_rate)

    return result

def get_rates_for_given_currencies(rates: dict, currencies: List[str]):
    return {currency: rates[currency] for currency in currencies if currency in rates}

@app.get("/get_currencies")
def get_currencies():
    return db_service.get_currencies()

@app.patch("/update_currency/{currency_id}")
def update_currency(currency_id: int, enabled: bool):
    return db_service.update_currency(currency_id, enabled)