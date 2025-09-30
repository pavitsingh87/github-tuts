import json
from fastapi import WebSocket
from models import (
    support_queue, active_support_sessions, 
    employee_connections, employee_status
)

async def request_human_support(user_id: str, user_ws: WebSocket):
    # Check if already in queue or session
    if user_id in active_support_sessions:
        await user_ws.send_text(json.dumps({
            "type": "system_message",
            "message": "You are already connected to a support agent."
        }))
        return
    
    if any(item['user_id'] == user_id for item in support_queue):
        await user_ws.send_text(json.dumps({
            "type": "system_message",
            "message": "You are already in the support queue."
        }))
        return
    
    # Add to support queue
    support_queue.append({
        "user_id": user_id,
        "user_ws": user_ws,
        "timestamp": json.dumps({"time": "now"})
    })
    
    await user_ws.send_text(json.dumps({
        "type": "system_message",
        "message": f"Added to support queue. Position: {len(support_queue)}"
    }))
    
    # Notify available employees
    await notify_employees_new_request()

async def notify_employees_new_request():
    for emp_id, emp_ws in employee_connections.items():
        if employee_status.get(emp_id) == 'available':
            try:
                await emp_ws.send_text(json.dumps({
                    "type": "queue_update",
                    "queue_length": len(support_queue)
                }))
            except:
                pass

async def assign_support_session(employee_id: str, employee_ws: WebSocket):
    if not support_queue:
        return False
    
    # Get first user from queue
    user_request = support_queue.pop(0)
    user_id = user_request['user_id']
    user_ws = user_request['user_ws']
    
    # Create active session
    active_support_sessions[user_id] = {
        "employee_id": employee_id,
        "employee_ws": employee_ws,
        "user_ws": user_ws
    }
    
    employee_status[employee_id] = 'busy'
    
    # Notify both parties
    await user_ws.send_text(json.dumps({
        "type": "support_connected",
        "employee_id": employee_id,
        "message": f"Connected to support agent {employee_id}"
    }))
    
    await employee_ws.send_text(json.dumps({
        "type": "customer_assigned",
        "user_id": user_id,
        "message": f"Customer {user_id} assigned to you"
    }))
    
    return True

async def end_support_session(user_id: str):
    if user_id in active_support_sessions:
        session = active_support_sessions[user_id]
        employee_id = session['employee_id']
        
        # Mark employee as available
        employee_status[employee_id] = 'available'
        
        # Notify both parties
        try:
            await session['user_ws'].send_text(json.dumps({
                "type": "support_ended",
                "message": "Support session ended"
            }))
        except:
            pass
        
        try:
            await session['employee_ws'].send_text(json.dumps({
                "type": "session_ended",
                "message": "Session ended"
            }))
        except:
            pass
        
        del active_support_sessions[user_id]