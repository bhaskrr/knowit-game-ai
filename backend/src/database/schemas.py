from pydantic import BaseModel

# Response model for a topic
class TopicResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        from_attributes = True