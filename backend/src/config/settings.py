import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL")

settings = Settings()