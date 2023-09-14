from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI

def setup_cors(app: FastAPI):
    """
    Set up CORS (Cross-Origin Resource Sharing) middleware for FastAPI.

    Args:
        app (FastAPI): The FastAPI application to add CORS middleware to.

    Raises:
        KeyError: If the "CORS_ORIGINS" environment variable is not set.
    """
    try:
        origins = os.environ["CORS_ORIGINS"].split(",")
    except KeyError:
        raise KeyError("The 'CORS_ORIGINS' environment variable is not set.")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
