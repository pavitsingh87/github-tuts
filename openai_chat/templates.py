def get_customer_home_template():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Finance Support - Customer Portal</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .hero-section { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            .feature-card { transition: transform 0.3s; }
            .feature-card:hover { transform: translateY(-5px); }
        </style>
    </head>
    <body class="bg-light">
        <div class="hero-section py-5">
            <div class="container">
                <div class="row justify-content-center text-center">
                    <div class="col-md-8">
                        <h1 class="display-4 mb-4">Finance Support Portal</h1>
                        <p class="lead">Get instant AI-powered finance assistance or connect with our expert support team</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card shadow feature-card">
                        <div class="card-body p-5">
                            <div class="text-center mb-4">
                                <i class="fas fa-comments fa-3x text-primary mb-3"></i>
                                <h3>Start Chat Session</h3>
                                <p class="text-muted">Connect with our AI assistant and support team</p>
                            </div>
                            <div class="mb-3">
                                <label class="form-label fw-bold">Your Name:</label>
                                <input id="username" type="text" class="form-control form-control-lg" placeholder="Enter your full name">
                            </div>
                            <div class="mb-4">
                                <label class="form-label fw-bold">Room ID (Optional):</label>
                                <input id="roomid" type="text" class="form-control form-control-lg" placeholder="Leave blank for general room">
                                <small class="text-muted">Join a specific room or use the default general room</small>
                            </div>
                            <button class="btn btn-primary btn-lg w-100" onclick="joinRoom()">Start Chat</button>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="row mt-5">
                <div class="col-md-4">
                    <div class="text-center">
                        <i class="fas fa-robot fa-2x text-success mb-3"></i>
                        <h5>AI Assistant</h5>
                        <p class="text-muted">Get instant answers to finance questions</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center">
                        <i class="fas fa-users fa-2x text-info mb-3"></i>
                        <h5>Human Support</h5>
                        <p class="text-muted">Connect with expert support agents</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center">
                        <i class="fas fa-clock fa-2x text-warning mb-3"></i>
                        <h5>24/7 Available</h5>
                        <p class="text-muted">Round-the-clock assistance</p>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="https://kit.fontawesome.com/your-fontawesome-kit.js"></script>
        <script>
            function joinRoom() {
                const username = document.getElementById('username').value.trim();
                const roomid = document.getElementById('roomid').value.trim() || 'general';
                if (!username) {
                    alert('Please enter your name');
                    return;
                }
                window.location.href = `/customer/chat/${roomid}/${username}`;
            }
            
            document.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') joinRoom();
            });
        </script>
    </body>
    </html>
    """

def get_employee_home_template():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Employee Portal - Finance Support</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .admin-header { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; }
            .login-card { max-width: 400px; margin: 0 auto; }
            .feature-icon { font-size: 2rem; color: #3498db; }
        </style>
    </head>
    <body class="bg-light">
        <div class="admin-header py-4">
            <div class="container">
                <div class="text-center">
                    <h2><i class="fas fa-shield-alt me-2"></i>Employee Portal</h2>
                    <p class="mb-0">Finance Support System - Staff Access</p>
                </div>
            </div>
        </div>
        
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="card shadow login-card">
                        <div class="card-header bg-primary text-white text-center">
                            <h4 class="mb-0"><i class="fas fa-user-tie me-2"></i>Staff Login</h4>
                        </div>
                        <div class="card-body p-4">
                            <div class="mb-4">
                                <label class="form-label fw-bold">Employee ID:</label>
                                <input id="employeeid" type="text" class="form-control form-control-lg" placeholder="Enter your employee ID">
                            </div>
                            <button class="btn btn-success btn-lg w-100" onclick="loginEmployee()">Access Dashboard</button>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="row mt-5">
                <div class="col-md-12">
                    <h4 class="text-center mb-4">Support Features</h4>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <i class="fas fa-headset feature-icon mb-3"></i>
                        <h6>Customer Support</h6>
                        <p class="text-muted small">Handle customer inquiries</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <i class="fas fa-list-ul feature-icon mb-3"></i>
                        <h6>Queue Management</h6>
                        <p class="text-muted small">Manage support queue</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <i class="fas fa-chart-line feature-icon mb-3"></i>
                        <h6>Real-time Stats</h6>
                        <p class="text-muted small">Monitor performance</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <i class="fas fa-comments feature-icon mb-3"></i>
                        <h6>Live Chat</h6>
                        <p class="text-muted small">Direct customer communication</p>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="https://kit.fontawesome.com/your-fontawesome-kit.js"></script>
        <script>
            function loginEmployee() {
                const employeeid = document.getElementById('employeeid').value.trim();
                if (!employeeid) {
                    alert('Please enter your employee ID');
                    return;
                }
                window.location.href = `/employee/dashboard/${employeeid}`;
            }
            
            document.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') loginEmployee();
            });
        </script>
    </body>
    </html>
    """

def get_chat_template(room_id: str, user_id: str):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Finance Chat - Room: {room_id}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f8f9fa; }}
            #chat-box {{
                border: 1px solid #ced4da;
                border-radius: 8px;
                padding: 15px;
                height: 400px;
                overflow-y: auto;
                background-color: #ffffff;
            }}
            .user-msg {{ color: #0d6efd; margin: 5px 0; }}
            .ai-msg {{ color: #198754; margin: 5px 0; }}
            .system-msg {{ color: #6c757d; margin: 5px 0; font-style: italic; }}
            .support-msg {{ color: #dc3545; margin: 5px 0; font-weight: bold; }}
            .chat-input-group {{ position: sticky; bottom: 0; background: #f8f9fa; padding-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="container py-4">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h4>Room: {room_id} | User: {user_id}</h4>
                <a href="/customer" class="btn btn-outline-secondary btn-sm">Leave Room</a>
            </div>
            <div id="chat-box" class="mb-3 shadow-sm"></div>
            <div class="input-group chat-input-group">
                <input id="message" type="text" class="form-control" placeholder="Type a message (finance questions get AI responses, '/human' for support)...">
                <button class="btn btn-primary" onclick="sendMessage()">Send</button>
                <button class="btn btn-warning" onclick="requestHuman()">Human Support</button>
            </div>
        </div>
        <script>
            const ws = new WebSocket(`ws://localhost:8000/customer/ws/{room_id}/{user_id}`);
            const chatBox = document.getElementById('chat-box');
            
            ws.onmessage = function(event) {{
                const data = JSON.parse(event.data);
                let msgClass = 'system-msg';
                let prefix = 'System';
                
                if (data.type === 'user_message') {{
                    msgClass = 'user-msg';
                    prefix = data.user_id;
                }} else if (data.type === 'ai_message') {{
                    msgClass = 'ai-msg';
                    prefix = 'AI Assistant';
                }} else if (data.type === 'support_message') {{
                    msgClass = 'support-msg';
                    prefix = 'Support Agent';
                }} else if (data.type === 'support_connected' || data.type === 'support_ended') {{
                    msgClass = 'system-msg';
                    prefix = 'System';
                }}
                
                chatBox.innerHTML += `<div class='${{msgClass}}'><b>${{prefix}}:</b> ${{data.message}}</div>`;
                chatBox.scrollTop = chatBox.scrollHeight;
            }};
            
            function sendMessage() {{
                const msg = document.getElementById('message').value.trim();
                if (!msg) return;
                
                ws.send(JSON.stringify({{ message: msg }}));
                document.getElementById('message').value = '';
            }}
            
            function requestHuman() {{
                ws.send(JSON.stringify({{ message: '/human' }}));
            }}
            
            document.getElementById('message').addEventListener('keypress', function(e) {{
                if (e.key === 'Enter') sendMessage();
            }});
            
            ws.onclose = function() {{
                chatBox.innerHTML += '<div class="system-msg"><b>System:</b> Connection closed</div>';
            }};
        </script>
    </body>
    </html>
    """

def get_employee_dashboard_template(employee_id: str):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Employee Dashboard - {employee_id}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f8f9fa; }}
            #chat-box {{
                border: 1px solid #ced4da;
                border-radius: 8px;
                padding: 15px;
                height: 400px;
                overflow-y: auto;
                background-color: #ffffff;
            }}
            .customer-msg {{ color: #0d6efd; margin: 5px 0; }}
            .employee-msg {{ color: #dc3545; margin: 5px 0; }}
            .system-msg {{ color: #6c757d; margin: 5px 0; font-style: italic; }}
        </style>
    </head>
    <body>
        <div class="container py-4">
            <div class="row">
                <div class="col-md-8">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h4>Employee: {employee_id}</h4>
                        <div>
                            <span id="status" class="badge bg-success">Available</span>
                            <a href="/" class="btn btn-outline-secondary btn-sm ms-2">Logout</a>
                        </div>
                    </div>
                    <div id="chat-box" class="mb-3 shadow-sm"></div>
                    <div class="input-group">
                        <input id="message" type="text" class="form-control" placeholder="Type your response..." disabled>
                        <button id="send-btn" class="btn btn-primary" onclick="sendMessage()" disabled>Send</button>
                        <button id="end-btn" class="btn btn-danger" onclick="endSession()" disabled>End Session</button>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-header">
                            <h5>Support Queue</h5>
                        </div>
                        <div class="card-body">
                            <div id="queue-info" class="mb-3">
                                <span id="queue-count">0</span> customers waiting
                            </div>
                            <button id="take-next-btn" class="btn btn-success w-100" onclick="takeNext()">Take Next Customer</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script>
            const ws = new WebSocket(`ws://localhost:8000/employee/ws/{employee_id}`);
            const chatBox = document.getElementById('chat-box');
            const messageInput = document.getElementById('message');
            const sendBtn = document.getElementById('send-btn');
            const endBtn = document.getElementById('end-btn');
            const takeNextBtn = document.getElementById('take-next-btn');
            const status = document.getElementById('status');
            const queueCount = document.getElementById('queue-count');
            
            let currentCustomer = null;
            
            ws.onmessage = function(event) {{
                const data = JSON.parse(event.data);
                
                if (data.type === 'customer_assigned') {{
                    currentCustomer = data.user_id;
                    chatBox.innerHTML += `<div class='system-msg'><b>System:</b> ${{data.message}}</div>`;
                    messageInput.disabled = false;
                    sendBtn.disabled = false;
                    endBtn.disabled = false;
                    takeNextBtn.disabled = true;
                    status.textContent = 'Busy';
                    status.className = 'badge bg-danger';
                }} else if (data.type === 'customer_message') {{
                    chatBox.innerHTML += `<div class='customer-msg'><b>${{data.user_id}}:</b> ${{data.message}}</div>`;
                }} else if (data.type === 'session_ended') {{
                    currentCustomer = null;
                    chatBox.innerHTML += `<div class='system-msg'><b>System:</b> ${{data.message}}</div>`;
                    messageInput.disabled = true;
                    sendBtn.disabled = true;
                    endBtn.disabled = true;
                    takeNextBtn.disabled = false;
                    status.textContent = 'Available';
                    status.className = 'badge bg-success';
                }} else if (data.type === 'queue_update') {{
                    queueCount.textContent = data.queue_length;
                }} else if (data.type === 'no_customers') {{
                    chatBox.innerHTML += `<div class='system-msg'><b>System:</b> ${{data.message}}</div>`;
                }}
                
                chatBox.scrollTop = chatBox.scrollHeight;
            }};
            
            function sendMessage() {{
                const msg = messageInput.value.trim();
                if (!msg || !currentCustomer) return;
                
                ws.send(JSON.stringify({{
                    action: 'send_message',
                    message: msg
                }}));
                
                chatBox.innerHTML += `<div class='employee-msg'><b>You:</b> ${{msg}}</div>`;
                messageInput.value = '';
                chatBox.scrollTop = chatBox.scrollHeight;
            }}
            
            function takeNext() {{
                ws.send(JSON.stringify({{ action: 'take_next' }}));
            }}
            
            function endSession() {{
                if (currentCustomer) {{
                    ws.send(JSON.stringify({{ action: 'end_session' }}));
                }}
            }}
            
            messageInput.addEventListener('keypress', function(e) {{
                if (e.key === 'Enter') sendMessage();
            }});
            
            ws.onclose = function() {{
                chatBox.innerHTML += '<div class="system-msg"><b>System:</b> Connection closed</div>';
            }};
        </script>
    </body>
    </html>
    """