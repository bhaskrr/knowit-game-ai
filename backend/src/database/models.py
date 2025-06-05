from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from backend.src.database.base import Base
from sqlalchemy.orm import relationship


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    questions = relationship("Question", back_populates="topic")


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question_text = Column(String)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    topic = relationship("Topic", back_populates="questions")
    options = relationship("Option", back_populates="question")


class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    option_text = Column(String)
    is_correct = Column(Boolean)
    question = relationship("Question", back_populates="options")
