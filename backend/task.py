import datetime
from fastapi_utils.tasks import repeat_every
from fastapi import FastAPI
from utils import fetch_remote_data
from database.models.exchange_rate import ExchangeRate
from db_service import DBService


async def daily_task():
    try:
        today = datetime.date.today().strftime("%Y-%m-%d")
        data = await fetch_remote_data(today)
        exchange_rate = ExchangeRate(date=today, rates=data)
        DBService().save_exchange_rate(exchange_rate)
        print(f"Daily task completed at {datetime.datetime.now()}")
    except Exception as e:
        print(e)


def setup_daily_task(app: FastAPI):
    # @app.on_event("startup")
    @repeat_every(seconds=60 * 60 * 24)  # Repeat every 24 hours (1 day)
    async def start_daily_task():
        await daily_task()