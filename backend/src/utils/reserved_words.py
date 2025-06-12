# forbidden_words.py
import os
import httpx
from typing import List
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

_cached_reserved_words: List[str] = []


def get_reserved_words() -> List[str]:
    global _cached_reserved_words

    if _cached_reserved_words:
        return _cached_reserved_words

    URL = os.environ.get("WORDS_URL", "")
    if not URL:
        raise RuntimeError("WORDS_URL env variable not set.")

    with httpx.Client(timeout=5.0) as client:
        response = client.get(URL)
        response.raise_for_status()
        _cached_reserved_words = response.json().get("RESERVED_WORDS", [])
    return _cached_reserved_words


def refresh_reserved_words():
    global _cached_reserved_words

    URL = os.environ.get("WORDS_URL", "")
    if not URL:
        raise RuntimeError("WORDS_URL env variable not set.")

    with httpx.Client(timeout=5.0) as client:
        response = client.get(URL)
        response.raise_for_status()
        _cached_reserved_words = response.json().get("RESERVED_WORDS", [])
