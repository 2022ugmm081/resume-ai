from pydantic import BaseModel
from typing import List, Optional


class Experience(BaseModel):
    """Work experience model"""
    company: str
    position: str
    duration: str
    description: str
    skills: Optional[List[str]] = []


class Education(BaseModel):
    """Education model"""
    institution: str
    degree: str
    field: str
    graduation_year: int
    gpa: Optional[float] = None


class Project(BaseModel):
    """Project model"""
    title: str
    description: str
    technologies: List[str]
    link: Optional[str] = None


class StudentProfile(BaseModel):
    """Student profile for resume generation"""
    full_name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    professional_summary: Optional[str] = None
    
    # Experience and Education
    education: List[Education]
    experiences: List[Experience] = []
    projects: List[Project] = []
    
    # Skills
    technical_skills: List[str] = []
    soft_skills: List[str] = []
    
    # Certifications
    certifications: List[str] = []
    
    # Languages
    languages: List[str] = []


class ResumeGenerationRequest(BaseModel):
    """Request for resume generation"""
    student_profile: StudentProfile
    style: Optional[str] = "professional"  # professional, creative, academic
    tone: Optional[str] = "formal"  # formal, casual, friendly


class ResumeContent(BaseModel):
    """Generated resume content"""
    professional_summary: str
    formatted_experience: str
    formatted_skills: str
    formatted_education: str
    additional_sections: Optional[str] = None
