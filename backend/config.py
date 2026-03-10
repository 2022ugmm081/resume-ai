"""
Configuration settings for the AI Resume SaaS backend
"""
import os
from typing import Optional


class Settings:
    """Application settings"""
    
    # API Configuration
    API_TITLE: str = "AI Resume Generator API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "Backend API for AI-powered resume generation using Groq"
    
    # Server Configuration
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    # Groq Configuration
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    GROQ_TEMPERATURE: float = float(os.getenv("GROQ_TEMPERATURE", "1.0"))
    GROQ_MAX_TOKENS: int = int(os.getenv("GROQ_MAX_TOKENS", "1024"))
    GROQ_TOP_P: float = float(os.getenv("GROQ_TOP_P", "1.0"))
    
    # Legacy LLM Configuration (for backward compatibility)
    LLM_API_KEY: Optional[str] = GROQ_API_KEY
    LLM_MODEL: str = GROQ_MODEL
    LLM_TEMPERATURE: float = GROQ_TEMPERATURE
    LLM_MAX_TOKENS: int = GROQ_MAX_TOKENS
    
    # PDF Configuration
    PDF_PAGE_SIZE: str = os.getenv("PDF_PAGE_SIZE", "letter")  # letter or A4
    PDF_MARGIN_INCH: float = float(os.getenv("PDF_MARGIN_INCH", "0.75"))
    PDF_STORAGE_PATH: str = os.getenv("PDF_STORAGE_PATH", "resumes")
    
    # Resume Configuration
    RESUME_DEFAULT_STYLE: str = os.getenv("RESUME_DEFAULT_STYLE", "professional")
    RESUME_DEFAULT_TONE: str = os.getenv("RESUME_DEFAULT_TONE", "formal")
    MAX_RESUME_TOKENS: int = int(os.getenv("MAX_RESUME_TOKENS", "2000"))
    
    # Database Configuration (optional)
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    # CORS Configuration
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:5000",
    ]
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
