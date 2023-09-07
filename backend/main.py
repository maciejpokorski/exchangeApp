from fastapi import FastAPI, HTTPException
from datetime import datetime
import os
import httpx

app = FastAPI()
API_KEY = os.getenv("API_KEY")

if (not API_KEY):
    raise EnvironmentError("API_KEY not provided") 

def build_openexchangerates_url_and_params(date: str):
    base_url = "https://openexchangerates.org/api/historical/"
    request_url = f"{base_url}{date}.json"
    request_params = {"app_id": API_KEY}
    return request_url, request_params

@app.get("/fetch_data/{date}")
async def fetch_data(date: str):
    # validate input date
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Date parameter must be valid and in YYYY-MM-DD format"}

    request_url, request_params = build_openexchangerates_url_and_params(date)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(request_url, params=request_params)

            # check if response is valid
            if response.status_code == 200:
                return response.json().get("rates")
            else:
                return {"error": "Failed to fetch data from the external API"}

        except httpx.RequestError as e:
            return {"error": f"Request error: {e}"}