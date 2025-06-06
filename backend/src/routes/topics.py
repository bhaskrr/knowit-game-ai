from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from backend.src.database.models import Topic, Question
from backend.src.database.crud import get_db
from backend.src.database.schemas import TopicResponse
from typing import List

# Create a new APIRouter instance for topic-related endpoints
topics_router = APIRouter()

@topics_router.post("/topics")
def create_topic(name: str, description: str, db: Session = Depends(get_db)):
    """
    Create a new topic in the database.

    Args:
        name (str): The name of the topic.
        description (str): A brief description of the topic.
        db (Session): SQLAlchemy database session (injected by FastAPI).

    Returns:
        Topic: The newly created Topic object.
    """
    topic = Topic(name=name, description=description)
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic

@topics_router.get("/topics", response_model=List[TopicResponse])
def get_topics(db: Session = Depends(get_db)):
    """
    Retrieve all topics from the database.

    Args:
        db (Session): SQLAlchemy database session (injected by FastAPI).

    Returns:
        List[TopicResponse]: A list of all topics as response models.
    """
    topics = db.query(Topic).all()
    results = [
        {
            "id": topic.id,
            "name": topic.name,
            "description": topic.description,
            "question_count": db.query(Question)
            .filter(Question.topic_id == topic.id)
            .count(),
        }
        for topic in topics
    ]
    return results