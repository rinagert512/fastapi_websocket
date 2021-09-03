from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
