from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from datetime import datetime
from typing import List
from utils import fetch_remote_data
from task import setup_daily_task
from cors import setup_cors
from database.service import (
    get_currencies,
    get_enabled_currencies,
    update_currency,
    get_exchange_rates,
)
from database.config import get_session, create_db_and_tables

app = FastAPI()
setup_cors(app)

@app.on_event("startup")
def init():
    create_db_and_tables()
    setup_daily_task(app)


@app.get("/fetch_remote_data/{date}")
async def fetch_data(date: str, session: Session = Depends(get_session)):
    """
    Fetch remote data for a given date and return exchange rates.

    Args:
        date (str): The date in YYYY-MM-DD format.
        session (Session): The SQLModel session.

    Returns:
        dict: A dictionary containing exchange rates for enabled currencies.
    """
    # Validate input date
    try:
        if datetime.strptime(date, "%Y-%m-%d") >= datetime.now():
            return {"error": "Date parameter must be in the past"}
    except ValueError:
        return {"error": "Date parameter must be valid and in YYYY-MM-DD format"}
    try:
        enabled_currencies = [c.code for c in get_enabled_currencies(session)]
        data = await fetch_remote_data(date)
        return get_rates_for_given_currencies(data, enabled_currencies)
    except Exception as e:
        return {"error": f"Request error: {e}"}


@app.get("/fetch_local_data/")
async def fetch_local_data(session: Session = Depends(get_session)):
    """
    Fetch local exchange rate data for enabled currencies.

    Args:
        session (Session): The SQLModel session.

    Returns:
        List[dict]: A list of dictionaries containing exchange rates for enabled currencies.
    """
    enabled_currencies = [c.code for c in get_enabled_currencies(session)]
    #if woulb be a lot of data, we should paginate the results
    data = get_exchange_rates(session)
    result = []
    for item in data:
        exchange_rate = {
            "Date": item.date,
        }
        exchange_rate.update(get_rates_for_given_currencies(item.rates, enabled_currencies))
        result.append(exchange_rate)

    return result


def get_rates_for_given_currencies(rates: dict, currencies: List[str]):
    """
    Filter exchange rates based on a list of currencies.

    Args:
        rates (dict): A dictionary of exchange rates.
        currencies (List[str]): List of currency codes to filter.

    Returns:
        dict: A dictionary containing filtered exchange rates.
    """
    return {currency: rates[currency] for currency in currencies if currency in rates}


@app.get("/get_currencies")
def currencies_get(session: Session = Depends(get_session)):
    """
    Get a list of available currencies.

    Args:
        session (Session): The SQLModel session.

    Returns:
        List[dict]: A list of dictionaries containing currency information.
    """
    return get_currencies(session)


@app.patch("/update_currency/{currency_id}")
def currency_update(currency_id: int, enabled: bool, session: Session = Depends(get_session)):
    """
    Update the status of a currency.

    Args:
        currency_id (int): The ID of the currency to update.
        enabled (bool): The new status for the currency (True for enabled, False for disabled).
        session (Session): The SQLModel session.

    Returns:
        dict: A dictionary indicating the success of the operation.
    """
    return update_currency(session, currency_id, enabled)
