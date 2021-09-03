from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)