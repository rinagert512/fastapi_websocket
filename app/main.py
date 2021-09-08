from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from . import schemas

app = FastAPI()

main_page = open('app/pages/index.html', 'r').read()

@app.get("/")
async def get():
    return HTMLResponse(main_page)

@app.websocket("/ws")
async def websocket_send_endpoint(websocket: WebSocket):
    await websocket.accept()

    messages = []
    while True:
        text = await websocket.receive_text()
        messages.append(text)
        await websocket.send_json([{
            'id': len(messages),
            'text': text
        }])
