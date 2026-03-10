from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from routes.chat import router as chat_router
from routes.resume import router as resume_router
from config import settings

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router)
app.include_router(resume_router)


@app.get("/")
def read_root():
    """Health check endpoint"""
    return {
        "message": "AI Resume Generator API is running",
        "version": settings.API_VERSION
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}