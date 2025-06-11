import os
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from backend.src.database.base import engine
from backend.src.database.models import Base
from backend.src.routes.topics import topics_router
from backend.src.routes.counts import counts_router
from backend.src.utils.forbidden_words import refresh_forbidden_words

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# Load the refresh api key to refresh cache
REFRESH_API_KEY = os.environ.get("FORBIDDEN_REFRESH_API_KEY", "")

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize the app
app = FastAPI()

origins = os.environ.get("ORIGINS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the routers
app.include_router(topics_router, tags=["topics"])
app.include_router(counts_router, tags=["counts"])

# Endpoints
@app.get("/health")
def health_check():
    """Health check endpoint to verify if the API is running"""
    return {"status": "ok", "message": "API is running"}


@app.post("/refresh-forbidden-words")
def trigger_refresh(request: Request):
    # Check the API key from headers
    api_key = request.headers.get("x-api-key")
    if api_key != REFRESH_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    refresh_forbidden_words()
    return {"message": "Forbidden words list refreshed successfully."}
