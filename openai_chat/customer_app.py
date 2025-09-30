from fastapi import FastAPI
from customer_routes import router

app = FastAPI(title="Finance Support - Customer Portal", version="1.0.0")

# Include customer routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)