from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from backend.src.database.models import Topic, Question
from backend.src.database.crud import get_db

# Create a router for counts related operations
counts_router = APIRouter()


@counts_router.get("/count")
def get_topic_count(db: Session = Depends(get_db)):
    topic_count = db.query(Topic).count()
    question_count = db.query(Question).count()
    return {
        "total_topics": topic_count,
        "total_questions": question_count,
    }
