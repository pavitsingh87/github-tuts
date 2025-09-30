from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from customer_routes import router as customer_router
from employee_routes import router as employee_router

app = FastAPI(title="Finance Support System", version="1.0.0")

# Landing page to direct users to appropriate portals
@app.get("/", response_class=HTMLResponse)
async def landing_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Finance Support System</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .hero-section { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; }
            .portal-card { transition: transform 0.3s; cursor: pointer; }
            .portal-card:hover { transform: translateY(-10px); }
        </style>
    </head>
    <body>
        <div class="hero-section d-flex align-items-center">
            <div class="container">
                <div class="row justify-content-center text-center">
                    <div class="col-md-10">
                        <h1 class="display-3 mb-4">Finance Support System</h1>
                        <p class="lead mb-5">Choose your portal to get started</p>
                        
                        <div class="row">
                            <div class="col-md-6 mb-4">
                                <div class="card portal-card shadow-lg h-100" onclick="window.location.href='/customer'">
                                    <div class="card-body p-5 text-dark">
                                        <i class="fas fa-user-circle fa-4x text-primary mb-4"></i>
                                        <h3 class="card-title">Customer Portal</h3>
                                        <p class="card-text">Get finance support, chat with AI assistant, or connect with support agents</p>
                                        <div class="btn btn-primary btn-lg">Enter Customer Portal</div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6 mb-4">
                                <div class="card portal-card shadow-lg h-100" onclick="window.location.href='/employee'">
                                    <div class="card-body p-5 text-dark">
                                        <i class="fas fa-user-tie fa-4x text-success mb-4"></i>
                                        <h3 class="card-title">Employee Portal</h3>
                                        <p class="card-text">Access staff dashboard, manage support queue, and assist customers</p>
                                        <div class="btn btn-success btn-lg">Enter Employee Portal</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="https://kit.fontawesome.com/your-fontawesome-kit.js"></script>
    </body>
    </html>
    """

# Include customer routes under /customer prefix
app.include_router(customer_router, prefix="/customer")

# Include employee routes under /employee prefix  
app.include_router(employee_router, prefix="/employee")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)