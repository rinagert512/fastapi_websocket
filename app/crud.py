from sqlalchemy.orm import Session

from . import models, schemas


def get_messages(db: Session):
    return db.query(models.Message).all()


def add_message(db: Session, text: str):
    message = models.Message(text=text)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
