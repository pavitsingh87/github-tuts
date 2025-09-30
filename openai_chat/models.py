from typing import Dict, List
from fastapi import WebSocket
from langchain.memory import ConversationBufferMemory

# Global state storage
user_memories: Dict[str, ConversationBufferMemory] = {}
room_connections: Dict[str, List[WebSocket]] = {}
user_info: Dict[WebSocket, Dict[str, str]] = {}

# Human Support System
support_queue: List[Dict] = []  # Users waiting for human support
active_support_sessions: Dict[str, Dict] = {}  # user_id -> {employee_id, employee_ws, user_ws}
employee_connections: Dict[str, WebSocket] = {}  # employee_id -> websocket
employee_status: Dict[str, str] = {}  # employee_id -> 'available'/'busy'