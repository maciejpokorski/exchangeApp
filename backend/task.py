from fastapi_utils.tasks import repeat_every
from fastapi import FastAPI


async def daily_task():
    # Replace this with your task logic
    print("Daily task executed!")

def setup_daily_task(app: FastAPI):
    @app.on_event("startup")
    @repeat_every(seconds=60 * 60 * 24)  # Repeat every 24 hours (1 day)
    async def start_daily_task():
        await daily_task()