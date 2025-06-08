import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    PROMPT_DIRECTORY = os.path.join("backend", "src", "prompt-templates")

settings = Settings()