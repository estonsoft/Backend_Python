from fastapi.middleware.cors import CORSMiddleware
import os

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")
allowed_origins_list = ALLOWED_ORIGINS.split(",")

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins= allowed_origins_list,  # Match frontend URL exactly
        allow_credentials=True,
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"],  # Explicitly allow OPTIONS
        allow_headers=["*"],
    )