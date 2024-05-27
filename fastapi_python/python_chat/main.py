from dataclasses import dataclass
import json
import uuid
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="python_chat/templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="python_chat/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_room(request: Request):
  return templates.TemplateResponse(request=request, name="index.html")


@dataclass
class ConnectionManager():
    def __init__(self):
        self.active_connections: dict = {}
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[uuid.uuid4()] = websocket
        await self.send_message(websocket, json.dumps({"isMe": True, "data": "You'he joined!", "username": "You"}))

    async def disconnect(self, websocket: WebSocket):
        for connection in self.active_connections.values():
            if connection == websocket:
                for con_id in self.active_connections.keys():
                    if self.active_connections[con_id] == connection:
                        del self.active_connections[con_id]
                        return con_id
    
    async def send_message(self, websocket: WebSocket, message: str):
        await websocket.send_text(message)

    async def broadcast(self, websocket: WebSocket, data: str):
        decoded_data = json.loads(data)

        for connection in self.active_connections.values():
            is_me = False
            if connection == websocket:
                is_me = True
            
            await connection.send_text(json.dumps({"isMe": is_me, "data": decoded_data["message"], "username": decoded_data["username"]}))

connection_manager = ConnectionManager()


@app.websocket("/message")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await connection_manager.broadcast(websocket, data)
    except WebSocketDisconnect:
        id = connection_manager.disconnect(websocket)
        return RedirectResponse("/")
    

