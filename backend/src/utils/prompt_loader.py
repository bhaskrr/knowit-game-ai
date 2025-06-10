import os
from string import Template
from backend.src.config.settings import settings


def load_trivia_generation_prompt(filename: str, variables: dict) -> str:
    prompt_path = os.path.join(settings.PROMPT_DIRECTORY, filename)
    with open(prompt_path, "r") as f:
        template = Template(f.read())
    return template.substitute(variables)