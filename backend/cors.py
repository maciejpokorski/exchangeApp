from fastapi.middleware.cors import CORSMiddleware
import os

def setup_cors(app):
    # throw exception if CORS_ORIGINS is not set
    origins = os.environ["CORS_ORIGINS"].split(",")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )