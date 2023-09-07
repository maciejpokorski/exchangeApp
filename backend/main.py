import os
from typing import Union
from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": os.getenv("API_KEY")}
