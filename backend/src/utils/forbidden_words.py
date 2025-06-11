# forbidden_words.py
import os
import httpx
from typing import List
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

_cached_forbidden_words: List[str] = []


def get_forbidden_words() -> List[str]:
    global _cached_forbidden_words

    if _cached_forbidden_words:
        return _cached_forbidden_words

    URL = os.environ.get("FORBIDDEN_WORDS_URL", "")
    if not URL:
        raise RuntimeError("FORBIDDEN_WORDS_URL env variable not set.")

    with httpx.Client(timeout=5.0) as client:
        response = client.get(URL)
        response.raise_for_status()
        _cached_forbidden_words = response.json().get("FORBIDDEN_WORDS", [])
    return _cached_forbidden_words


def refresh_forbidden_words():
    global _cached_forbidden_words

    URL = os.environ.get("FORBIDDEN_WORDS_URL", "")
    if not URL:
        raise RuntimeError("FORBIDDEN_WORDS_URL env variable not set.")

    with httpx.Client(timeout=5.0) as client:
        response = client.get(URL)
        response.raise_for_status()
        _cached_forbidden_words = response.json().get("FORBIDDEN_WORDS", [])
