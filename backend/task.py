import datetime
from fastapi_utils.tasks import repeat_every
from fastapi import FastAPI, Depends
from sqlmodel import Session
from database.config import engine
from utils import fetch_remote_data
from database.models.exchange_rate import ExchangeRate
from database.service import save_exchange_rate

async def daily_task():
    """
    Perform a daily task to fetch and save exchange rate data.

    This function is scheduled to run once a day.

    Raises:
        Exception: If an error occurs during the task.
    """
    try:
        today = datetime.date.today().strftime("%Y-%m-%d")
        data = await fetch_remote_data(today)
        exchange_rate = ExchangeRate(date=today, rates=data)
        with Session(engine) as session:
            save_exchange_rate(session, exchange_rate)
        print(f"Daily task completed at {datetime.datetime.now()}")
    except Exception as e:
        print(e)

def setup_daily_task(app: FastAPI):
    """
    Set up a daily task to run the `daily_task` function.

    Args:
        app (FastAPI): The FastAPI application to add the task to.
    """
    @app.on_event("startup")
    @repeat_every(seconds=60 * 60 * 24)  # Repeat every 24 hours (1 day)
    async def start_daily_task():
        await daily_task()
