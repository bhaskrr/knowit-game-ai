from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from backend.src.config.settings import settings

# Get the database url
DATABASE_URL = settings.DATABASE_URL

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

# Base class for models to inherit from
Base = declarative_base()