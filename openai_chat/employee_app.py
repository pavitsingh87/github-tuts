from fastapi import FastAPI
from employee_routes import router

app = FastAPI(title="Finance Support - Employee Portal", version="1.0.0")

# Include employee routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)