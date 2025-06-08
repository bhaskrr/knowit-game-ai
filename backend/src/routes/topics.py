from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from backend.src.database.models import Topic, Question
from backend.src.database.crud import get_db
from backend.src.utils.schemas import TopicResponse, QuestionResponse
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

@topics_router.get("/topics/{topic_id}/trivia", response_model= List[QuestionResponse])
def get_trivia_questions(topic_id: int, limit: int = 5, db: Session = Depends(get_db)):
    """Retrieve a specified number of random questions for a topic
    
    Args:
        topic_id (int): id of the topic
        limit (int): number of questions to fetch
        db (Session): SQLAlchemy database session (injected by FastAPI).
    
    Returns:
        A list of questions with 
    """
    topic = db.query(Topic).filter_by(id=topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found!")

    questions = (
        db.query(Question)
        .filter_by(topic_id=topic_id)
        .order_by(func.random())
        .limit(limit)
        .all()
    )

    return [
        {
            "id": q.id,
            "text": q.question_text,
            "options": [
                {
                    "id": opt.id,
                    "text": opt.option_text,
                    "is_correct": opt.is_correct,
                }
                for opt in q.options
            ],
        }
        for q in questions
    ]
