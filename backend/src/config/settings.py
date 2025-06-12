import os
from dotenv import find_dotenv, load_dotenv
from backend.src.utils.forbidden_words import get_forbidden_words
from backend.src.utils.reserved_words import get_reserved_words

load_dotenv(find_dotenv())

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    PROMPT_DIRECTORY = os.path.join("backend", "src", "prompt-templates")
    FORBIDDEN_WORDS = get_forbidden_words()
    RESERVED_WORDS = get_reserved_words()

settings = Settings()