from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List
from task import setup_daily_task
from cors import setup_cors
from constants import DEFAULT_CURRENCIES, API_KEY
import httpx

app = FastAPI()

# init
setup_cors(app)
setup_daily_task(app)

def build_openexchangerates_url_and_params(date: str):
    base_url = "https://openexchangerates.org/api/historical/"
    request_url = f"{base_url}{date}.json"
    request_params = {"app_id": API_KEY}
    return request_url, request_params

@app.get("/fetch_data/{date}")
async def fetch_data(date: str, currency: List[str] = Query(DEFAULT_CURRENCIES)):
    # validate input date
    try:
        if datetime.strptime(date, "%Y-%m-%d") >= datetime.now():
            return {"error": "Date parameter must be in the past"}
    except ValueError:
        return {"error": "Date parameter must be valid and in YYYY-MM-DD format"}

    request_url, request_params = build_openexchangerates_url_and_params(date)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(request_url, params=request_params)

            # check if response is valid
            if response.status_code == 200:
                rates = response.json().get("rates")
                return get_rates_for_given_currencies(rates, currency)
            else:
                return {"error": "Failed to fetch data from the external API"}

        except httpx.RequestError as e:
            return {"error": f"Request error: {e}"}

def get_rates_for_given_currencies(rates: dict, currencies: List[str]):
    return {currency: rates[currency] for currency in currencies if currency in rates}