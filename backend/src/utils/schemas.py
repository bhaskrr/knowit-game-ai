from pydantic import BaseModel, Field
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

class TriviaGenerationInput(BaseModel):
    name: str

class GeneratedOption(BaseModel):
    option_text: str
    is_correct: bool


class GeneratedQuestion(BaseModel):
    question_text: str
    options: List[GeneratedOption]


class GeneratedTrivia(BaseModel):
    name: str = Field(..., min_length=5, max_length=20)
    description: str = Field(..., min_length=130, max_length=220)
    questions: List[GeneratedQuestion]

