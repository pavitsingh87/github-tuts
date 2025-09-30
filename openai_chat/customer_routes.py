from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
from websocket_handlers import handle_customer_websocket
from templates import get_customer_home_template, get_chat_template

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def customer_home():
    return get_customer_home_template()

@router.get("/chat/{room_id}/{user_id}", response_class=HTMLResponse)
async def chat_room(room_id: str, user_id: str):
    return get_chat_template(room_id, user_id)

@router.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, user_id: str):
    await handle_customer_websocket(websocket, room_id, user_id)