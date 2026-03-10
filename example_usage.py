"""
Example usage of the AI Resume Generator API

This file demonstrates how to use the resume generation endpoints.
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/resume"


# Example student profile
student_profile = {
    "full_name": "John Doe",
    "email": "john.doe@email.com",
    "phone": "+1-234-567-8900",
    "location": "San Francisco, CA",
    "professional_summary": "Passionate software engineer with 3+ years of experience",
    
    "education": [
        {
            "institution": "University of California, Berkeley",
            "degree": "Bachelor of Science",
            "field": "Computer Science",
            "graduation_year": 2021,
            "gpa": 3.8
        }
    ],
    
    "experiences": [
        {
            "company": "Tech Company Inc.",
            "position": "Software Engineer",
            "duration": "2021 - Present",
            "description": "Developed and maintained microservices using Python and FastAPI. Implemented CI/CD pipelines and improved system performance by 40%.",
            "skills": ["Python", "FastAPI", "Docker", "AWS"]
        },
        {
            "company": "StartUp XYZ",
            "position": "Junior Developer",
            "duration": "2020 - 2021",
            "description": "Built RESTful APIs and worked with React frontend team. Contributed to database optimization.",
            "skills": ["JavaScript", "Node.js", "MongoDB"]
        }
    ],
    
    "projects": [
        {
            "title": "AI Resume Generator",
            "description": "Built an intelligent resume generator using Groq API and LLM. Generates personalized professional summaries and highlights for students.",
            "technologies": ["Python", "FastAPI", "Groq API", "ReportLab"],
            "link": "https://github.com/example/ai-resume-generator"
        },
        {
            "title": "E-commerce Platform",
            "description": "Developed full-stack e-commerce platform with payment integration and real-time inventory management.",
            "technologies": ["React", "Node.js", "MongoDB", "Stripe"],
            "link": "https://github.com/example/ecommerce-platform"
        }
    ],
    
    "technical_skills": [
        "Python",
        "JavaScript",
        "FastAPI",
        "React",
        "Docker",
        "AWS",
        "PostgreSQL",
        "MongoDB",
        "Git"
    ],
    
    "soft_skills": [
        "Leadership",
        "Team Collaboration",
        "Problem Solving",
        "Communication",
        "Project Management"
    ],
    
    "certifications": [
        "AWS Certified Solutions Architect - Associate",
        "Google Cloud Associate Cloud Engineer"
    ],
    
    "languages": ["English", "Spanish", "Mandarin"]
}


def example_generate_resume():
    """Generate and return resume content"""
    payload = {
        "student_profile": student_profile,
        "style": "professional",
        "tone": "formal"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/generate",
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        
        print("=" * 70)
        print("RESUME GENERATION RESULT")
        print("=" * 70)
        print(json.dumps(result, indent=2))
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def example_generate_pdf():
    """Generate resume as PDF file"""
    payload = {
        "student_profile": student_profile,
        "style": "professional",
        "tone": "formal"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/generate-pdf",
            json=payload
        )
        response.raise_for_status()
        
        # Save PDF to file
        filename = f"{student_profile['full_name'].lower().replace(' ', '_')}_resume.pdf"
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"PDF resume saved as: {filename}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False


def example_preview_resume():
    """Preview resume content without generating PDF"""
    payload = {
        "student_profile": student_profile,
        "style": "professional",
        "tone": "formal"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/preview",
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        
        print("=" * 70)
        print("RESUME PREVIEW")
        print("=" * 70)
        print(result['content'])
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print("Make sure the server is running: python -m uvicorn ai_backend.main:app --reload")
    print()
    
    # Uncomment the example you want to run:
    
    # example_generate_resume()
    # example_preview_resume()
    # example_generate_pdf()
