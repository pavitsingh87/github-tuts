from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
from websocket_handlers import handle_customer_websocket, handle_employee_websocket
from templates import get_home_template, get_chat_template, get_employee_template

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    return get_home_template()

@router.get("/chat/{room_id}/{user_id}", response_class=HTMLResponse)
async def chat_room(room_id: str, user_id: str):
    return get_chat_template(room_id, user_id)

@router.get("/employee/{employee_id}", response_class=HTMLResponse)
async def employee_dashboard(employee_id: str):
    return get_employee_template(employee_id)

@router.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, user_id: str):
    await handle_customer_websocket(websocket, room_id, user_id)

@router.websocket("/employee/{employee_id}")
async def employee_websocket(websocket: WebSocket, employee_id: str):
    await handle_employee_websocket(websocket, employee_id)