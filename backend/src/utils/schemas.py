from pydantic import BaseModel
from typing import List

# Response model for a topic
class TopicResponse(BaseModel):
    id: int
    name: str
    description: str
    question_count: int
    class Config:
        from_attributes = True


class Option(BaseModel):
    id: int
    text: str
    is_correct: bool


class QuestionResponse(BaseModel):
    id: int
    text: str
    options: List[Option]
    
    class Config:
        from_attributes = True

class TopicGenerationInput(BaseModel):
    name: str