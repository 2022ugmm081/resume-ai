from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import logging
from datetime import datetime
import os

from schemas.resume_schema import ResumeGenerationRequest, StudentProfile, ResumeContent
from services.resume_service import generate_complete_resume, format_resume_for_pdf
from services.pdf_service import create_resume_pdf, save_resume_to_file

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/resume", tags=["resume"])


@router.post("/generate")
async def generate_resume(request: ResumeGenerationRequest):
    """
    Generate a complete resume using AI and return the formatted content
    """
    try:
        # Generate resume content using Groq
        resume_content = generate_complete_resume(
            profile=request.student_profile,
            style=request.style or "professional",
            tone=request.tone or "formal"
        )
        
        logger.info(f"Resume generated successfully for {request.student_profile.full_name}")
        
        return {
            "success": True,
            "message": "Resume generated successfully",
            "data": resume_content
        }
    
    except Exception as e:
        logger.error(f"Error generating resume: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating resume: {str(e)}")


@router.post("/generate-pdf")
async def generate_pdf_resume(request: ResumeGenerationRequest):
    """
    Generate a complete resume and return as PDF file
    """
    try:
        student_name = request.student_profile.full_name
        
        # Generate resume content using Groq
        resume_content = generate_complete_resume(
            profile=request.student_profile,
            style=request.style or "professional",
            tone=request.tone or "formal"
        )
        
        # Format content for PDF
        formatted_content = format_resume_for_pdf(request.student_profile, resume_content)
        
        # Create PDF
        pdf_bytes = create_resume_pdf(student_name, formatted_content)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = student_name.lower().replace(" ", "_")
        filename = f"{safe_name}_{timestamp}"
        
        # Save PDF to file
        filepath = save_resume_to_file(pdf_bytes, filename)
        
        logger.info(f"PDF resume generated for {student_name}")
        
        return FileResponse(
            path=filepath,
            filename=f"{safe_name}_resume.pdf",
            media_type="application/pdf"
        )
    
    except Exception as e:
        logger.error(f"Error generating PDF resume: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF resume: {str(e)}")


@router.post("/preview")
async def preview_resume(request: ResumeGenerationRequest):
    """
    Preview the formatted resume content without generating PDF
    """
    try:
        # Generate resume content using Groq
        resume_content = generate_complete_resume(
            profile=request.student_profile,
            style=request.style or "professional",
            tone=request.tone or "formal"
        )
        
        # Format content
        formatted_content = format_resume_for_pdf(request.student_profile, resume_content)
        
        logger.info(f"Resume preview generated for {request.student_profile.full_name}")
        
        return {
            "success": True,
            "message": "Resume preview generated successfully",
            "content": formatted_content,
            "metadata": {
                "name": request.student_profile.full_name,
                "email": request.student_profile.email,
                "style": request.style or "professional",
                "tone": request.tone or "formal"
            }
        }
    
    except Exception as e:
        logger.error(f"Error previewing resume: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error previewing resume: {str(e)}")
