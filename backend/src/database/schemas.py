from pydantic import BaseModel

# Response model for a topic
class TopicResponse(BaseModel):
    id: int
    name: str
    description: str
    question_count: int
    
    class Config:
        from_attributes = True