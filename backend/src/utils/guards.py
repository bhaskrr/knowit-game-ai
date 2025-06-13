import re
from backend.src.utils.schemas import GeneratedTrivia, GeneratedQuestion
from backend.src.config.settings import settings

# These are forbidden
FORBIDDEN_WORDS = settings.FORBIDDEN_WORDS

# These are reserved
RESERVED_WORDS = settings.RESERVED_WORDS


def contains_reserved_word(topic: str) -> bool:
    topic_lower = topic.lower()
    for word in RESERVED_WORDS:
        # Use regex to match whole words only
        if re.search(rf"\b{re.escape(word)}\b", topic_lower):
            return True
    return False


def topic_exists_in_db(topic) -> bool:
    """Checks if the specified topic exists in the database."""
    # ! Yet to implement
    return False


def is_input_topic_valid(topic: str):
    "Checks if the input topic is valid."

    if contains_reserved_word(topic):
        return {"Error": "Topic name contains reserved words."}

    if topic_exists_in_db(topic):
        return {"Error": "A similar topic exists in the database."}

    if any(word in topic for word in FORBIDDEN_WORDS):
        return False

    if "  " in topic:
        return {"Error": "Topic name cannot contain consecutive spaces."}

    return True
    # TODO: Might need to add more checks


def is_question_valid(question: GeneratedQuestion) -> bool:
    """Checks if a question is valid"""
    # Get the question text and options
    text = question.question_text.strip()
    options = question.options

    # Check if the text is empty
    if not text:
        return False

    # Check if the question text contains any forbidden words
    if any(word in text.lower() for word in FORBIDDEN_WORDS):
        return False

    # Check if there are different number of options than 4
    if len(options) != 4:
        return False

    # Check if any of the options are duplicate
    option_texts = [option.option_text.strip() for option in options]
    if len(set(option_texts)) != 4 or "" in option_texts:
        return False

    # Check if more than one option is marked true
    correct_count = sum(1 for option in options if option.is_correct is True)
    if correct_count != 1:
        return False

    # * If none of the above checks fail, the question is valid
    return True


def is_output_valid(topic: GeneratedTrivia) -> bool:
    """Checks if the topic is valid"""
    name = topic.name
    questions = topic.questions
    # Check if the name contains any forbidden words
    if any(word in name for word in FORBIDDEN_WORDS):
        return False

    # Check if there are different number of questions than specified
    # ! 5 is the default limit
    if len(questions) != 5:
        return False

    # Check if any of the questions are duplicate
    question_texts = [ques.question_text for ques in questions]
    if len(set(question_texts)) != 5 or "" in question_texts:
        return False

    # Check whether individual questions are valid
    if not all(is_question_valid(question) for question in questions):
        return False

    # * At this point, the topic is valid
    return True
