import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.database.base import engine
from backend.src.database.models import Base
from backend.src.routes.topics import topics_router
from backend.src.routes.counts import counts_router

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

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