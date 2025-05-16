from fastapi import FastAPI
from app.api.v1.routes import router as api_router
from app.core.config import settings

app = FastAPI(title="Sentiment Analysis API")

@app.on_event("startup")
async def startup_event():
    print("Application starting...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutting down...")

app.include_router(api_router, prefix="/api/v1")
