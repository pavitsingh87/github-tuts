from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
from websocket_handlers import handle_employee_websocket
from templates import get_employee_home_template, get_employee_dashboard_template

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def employee_home():
    return get_employee_home_template()

@router.get("/dashboard/{employee_id}", response_class=HTMLResponse)
async def employee_dashboard(employee_id: str):
    return get_employee_dashboard_template(employee_id)

@router.websocket("/ws/{employee_id}")
async def employee_websocket(websocket: WebSocket, employee_id: str):
    await handle_employee_websocket(websocket, employee_id)