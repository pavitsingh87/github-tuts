import json
from fastapi import WebSocket, WebSocketDisconnect
from models import (
    room_connections, user_info, active_support_sessions,
    employee_connections, employee_status
)
from ai_service import get_user_agent, is_finance_question
from support_service import (
    request_human_support, assign_support_session, 
    end_support_session
)

async def broadcast_to_room(room_id: str, message: dict, exclude: WebSocket = None):
    if room_id in room_connections:
        for connection in room_connections[room_id].copy():
            if connection != exclude:
                try:
                    await connection.send_text(json.dumps(message))
                except:
                    room_connections[room_id].remove(connection)

async def handle_customer_websocket(websocket: WebSocket, room_id: str, user_id: str):
    await websocket.accept()
    
    # Add user to room
    if room_id not in room_connections:
        room_connections[room_id] = []
    room_connections[room_id].append(websocket)
    user_info[websocket] = {"user_id": user_id, "room_id": room_id}
    
    # Notify room of new user
    await broadcast_to_room(room_id, {
        "type": "user_joined",
        "user_id": user_id,
        "message": f"{user_id} joined the room"
    }, exclude=websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            user_message = message_data.get("message", "").strip()
            
            # Broadcast user message to room
            await broadcast_to_room(room_id, {
                "type": "user_message",
                "user_id": user_id,
                "message": user_message
            })
            
            # Handle special commands
            if user_message.lower() == "/human":
                await request_human_support(user_id, websocket)
                continue
            
            # Check if user is in active support session
            if user_id in active_support_sessions:
                # Forward message to assigned employee
                session = active_support_sessions[user_id]
                employee_ws = session['employee_ws']
                try:
                    await employee_ws.send_text(json.dumps({
                        "type": "customer_message",
                        "user_id": user_id,
                        "message": user_message
                    }))
                except:
                    # Employee disconnected, return to queue
                    await end_support_session(user_id)
                continue
            
            # Check if it's a finance question for AI response
            if is_finance_question(user_message):
                try:
                    agent = get_user_agent(user_id)
                    ai_response = agent.run(user_message)
                    
                    # Check if AI suggests human support
                    if "contact support" in ai_response.lower() or "human agent" in ai_response.lower():
                        ai_response += "\n\nType '/human' to connect with a human support agent."
                    
                    await broadcast_to_room(room_id, {
                        "type": "ai_message",
                        "user_id": "AI Assistant",
                        "message": ai_response
                    })
                except Exception as e:
                    await broadcast_to_room(room_id, {
                        "type": "ai_message",
                        "user_id": "AI Assistant",
                        "message": "Sorry, I encountered an error. Type '/human' for human support."
                    })
                    
    except WebSocketDisconnect:
        # Remove user from room
        room_connections[room_id].remove(websocket)
        del user_info[websocket]
        
        # Notify room of user leaving
        await broadcast_to_room(room_id, {
            "type": "user_left",
            "user_id": user_id,
            "message": f"{user_id} left the room"
        })
        
        # Clean up empty rooms
        if not room_connections[room_id]:
            del room_connections[room_id]

async def handle_employee_websocket(websocket: WebSocket, employee_id: str):
    await websocket.accept()
    employee_connections[employee_id] = websocket
    employee_status[employee_id] = 'available'
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            action = message_data.get("action")
            
            if action == "take_next":
                success = await assign_support_session(employee_id, websocket)
                if not success:
                    await websocket.send_text(json.dumps({
                        "type": "no_customers",
                        "message": "No customers in queue"
                    }))
            
            elif action == "send_message":
                # Find customer for this employee
                customer_id = None
                for uid, session in active_support_sessions.items():
                    if session['employee_id'] == employee_id:
                        customer_id = uid
                        break
                
                if customer_id:
                    customer_ws = active_support_sessions[customer_id]['user_ws']
                    try:
                        await customer_ws.send_text(json.dumps({
                            "type": "support_message",
                            "employee_id": employee_id,
                            "message": message_data.get("message", "")
                        }))
                    except:
                        await end_support_session(customer_id)
            
            elif action == "end_session":
                # Find and end customer session
                for uid, session in active_support_sessions.items():
                    if session['employee_id'] == employee_id:
                        await end_support_session(uid)
                        break
                        
    except WebSocketDisconnect:
        # Clean up employee connection
        if employee_id in employee_connections:
            del employee_connections[employee_id]
        if employee_id in employee_status:
            del employee_status[employee_id]
        
        # End any active sessions
        for uid, session in list(active_support_sessions.items()):
            if session['employee_id'] == employee_id:
                await end_support_session(uid)