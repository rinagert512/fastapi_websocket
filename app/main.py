from typing import List

from fastapi import Depends, FastAPI, HTTPException, WebSocket
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

main_page = open('app/pages/index.html', 'r').read()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def get():
    return HTMLResponse(main_page)

@app.websocket("/ws")
async def websocket_send_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()

    messages = crud.get_messages(db=db)
    data = []
    for msg in messages:
        data.append({
            "id": msg.id,
            "text": msg.text
        })
    await websocket.send_json(data)

    while True:
        text = await websocket.receive_text()
        msg = crud.add_message(db=db, text=text)
        data = [{
            "id": msg.id,
            "text": msg.text
        }]
        await websocket.send_json(data)
