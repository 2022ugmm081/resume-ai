"""
Comprehensive API Examples for AI Resume Generator

This file contains detailed examples of how to use the AI Resume Generator API
with different scenarios, styles, and tones.
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/resume"


# ============================================================================
# EXAMPLE 1: Entry-Level Software Engineer
# ============================================================================

ENTRY_LEVEL_ENGINEER = {
    "student_profile": {
        "full_name": "Alex Johnson",
        "email": "alex.johnson@email.com",
        "phone": "+1-234-567-8900",
        "location": "San Jose, CA",
        
        "education": [
            {
                "institution": "University of California, San Jose",
                "degree": "Bachelor of Science",
                "field": "Computer Science",
                "graduation_year": 2023,
                "gpa": 3.75
            }
        ],
        
        "experiences": [
            {
                "company": "TechCorp Solutions",
                "position": "Junior Software Engineer",
                "duration": "2023 - Present",
                "description": "Develop features for internal tools using Python and FastAPI framework. Participate in code reviews and contribute to technical documentation.",
                "skills": ["Python", "FastAPI", "REST APIs", "Git"]
            },
            {
                "company": "StartupXYZ",
                "position": "Intern - Full Stack Developer",
                "duration": "Summer 2022",
                "description": "Built frontend components with React and integrated with backend APIs. Improved page load time by 30%.",
                "skills": ["React", "JavaScript", "Node.js", "MongoDB"]
            }
        ],
        
        "projects": [
            {
                "title": "Task Management App",
                "description": "Full-stack web application for team collaboration. Features include real-time updates and user authentication.",
                "technologies": ["React", "Node.js", "PostgreSQL", "Socket.io"],
                "link": "https://github.com/alexjohnson/task-manager"
            }
        ],
        
        "technical_skills": [
            "Python", "JavaScript", "React", "Node.js", "FastAPI",
            "PostgreSQL", "MongoDB", "REST APIs", "Git", "Docker"
        ],
        "soft_skills": ["Communication", "Team Collaboration", "Problem Solving"],
        "certifications": ["AWS Certified Developer Associate"],
        "languages": ["English", "Spanish"]
    },
    "style": "professional",
    "tone": "formal"
}


# ============================================================================
# EXAMPLE 2: Mid-Level Data Scientist
# ============================================================================

MID_LEVEL_DATA_SCIENTIST = {
    "student_profile": {
        "full_name": "Sarah Chen",
        "email": "sarah.chen@email.com",
        "phone": "+1-555-234-5678",
        "location": "New York, NY",
        
        "education": [
            {
                "institution": "New York University",
                "degree": "Master of Science",
                "field": "Data Science",
                "graduation_year": 2022,
                "gpa": 3.8
            },
            {
                "institution": "University of Michigan",
                "degree": "Bachelor of Science",
                "field": "Statistics",
                "graduation_year": 2020,
                "gpa": 3.7
            }
        ],
        
        "experiences": [
            {
                "company": "FinanceCorp Analytics",
                "position": "Senior Data Scientist",
                "duration": "2022 - Present",
                "description": "Lead machine learning initiatives for risk prediction models. Improved model accuracy by 15% using ensemble methods. Mentored junior data scientists.",
                "skills": ["Python", "Machine Learning", "SQL", "Tableau", "AWS"]
            },
            {
                "company": "DataInsights Inc.",
                "position": "Data Scientist",
                "duration": "2020 - 2022",
                "description": "Developed ETL pipelines and built predictive models. Created dashboards for C-level executives.",
                "skills": ["Python", "TensorFlow", "Spark", "BigQuery"]
            }
        ],
        
        "projects": [
            {
                "title": "Credit Risk Prediction Model",
                "description": "Built machine learning model to predict loan defaults with 92% accuracy using LightGBM and ensemble techniques.",
                "technologies": ["Python", "Scikit-Learn", "LightGBM", "XGBoost"],
                "link": "https://github.com/sarahchen/credit-risk-model"
            },
            {
                "title": "Real-time Data Pipeline",
                "description": "Designed and implemented streaming data pipeline processing 1M+ events per day.",
                "technologies": ["Apache Kafka", "PySpark", "Airflow", "AWS S3"],
                "link": None
            }
        ],
        
        "technical_skills": [
            "Python", "R", "SQL", "Machine Learning", "TensorFlow", "PyTorch",
            "Scikit-Learn", "Spark", "Airflow", "Tableau", "Power BI", "AWS", "GCP"
        ],
        "soft_skills": [
            "Leadership", "Communication", "Strategic Thinking", "Data Storytelling"
        ],
        "certifications": [
            "AWS Certified Machine Learning Specialist",
            "Google Cloud Professional Data Engineer"
        ],
        "languages": ["English", "Mandarin", "Japanese"]
    },
    "style": "professional",
    "tone": "formal"
}


# ============================================================================
# EXAMPLE 3: Creative Designer with Portfolio
# ============================================================================

CREATIVE_DESIGNER = {
    "student_profile": {
        "full_name": "Marcus Williams",
        "email": "marcus.williams@email.com",
        "phone": "+1-424-555-0123",
        "location": "Los Angeles, CA",
        
        "education": [
            {
                "institution": "Art Center College of Design",
                "degree": "Bachelor of Fine Arts",
                "field": "Graphic Design",
                "graduation_year": 2021,
                "gpa": 3.6
            }
        ],
        
        "experiences": [
            {
                "company": "Creative Agency Co.",
                "position": "Senior UX/UI Designer",
                "duration": "2021 - Present",
                "description": "Lead design of mobile and web applications for Fortune 500 clients. Increased user engagement by 40% through UX improvements.",
                "skills": ["Figma", "UI/UX Design", "Prototyping", "User Research"]
            },
            {
                "company": "Digital Studio",
                "position": "Graphic Designer",
                "duration": "2020 - 2021",
                "description": "Created visual content for marketing campaigns and brand identity development.",
                "skills": ["Adobe Creative Suite", "Branding", "Print Design"]
            }
        ],
        
        "projects": [
            {
                "title": "Mobile App Redesign",
                "description": "Complete UX/UI redesign of fintech mobile app resulting in 45% increase in user retention.",
                "technologies": ["Figma", "iOS", "Material Design"],
                "link": "https://dribbble.com/marcuswilliams"
            }
        ],
        
        "technical_skills": [
            "Figma", "Adobe XD", "Photoshop", "Illustrator", "InDesign",
            "Prototyping", "User Research", "Wireframing", "CSS", "HTML"
        ],
        "soft_skills": [
            "Creativity", "Communication", "Client Management", "Time Management"
        ],
        "certifications": ["Google UX Design Certificate"],
        "languages": ["English", "Portuguese"]
    },
    "style": "creative",
    "tone": "casual"
}


# ============================================================================
# EXAMPLE 4: Academic/Research Profile
# ============================================================================

ACADEMIC_RESEARCHER = {
    "student_profile": {
        "full_name": "Dr. Emily Rodriguez",
        "email": "e.rodriguez@email.com",
        "phone": "+1-617-555-0101",
        "location": "Boston, MA",
        
        "education": [
            {
                "institution": "MIT (Massachusetts Institute of Technology)",
                "degree": "PhD",
                "field": "Computer Science - AI/ML",
                "graduation_year": 2023,
                "gpa": 3.9
            },
            {
                "institution": "Stanford University",
                "degree": "Bachelor of Science",
                "field": "Computer Science",
                "graduation_year": 2019,
                "gpa": 3.8
            }
        ],
        
        "experiences": [
            {
                "company": "MIT CSAIL - Artificial Intelligence Lab",
                "position": "Research Scientist",
                "duration": "2023 - Present",
                "description": "Conduct research on interpretable machine learning. Published 5 papers at top-tier conferences.",
                "skills": ["Machine Learning", "Research", "Python", "PyTorch"]
            },
            {
                "company": "Stanford University",
                "position": "Graduate Research Assistant",
                "duration": "2019 - 2023",
                "description": "Worked on neural architecture search and model optimization under Prof. Andrew Ng.",
                "skills": ["Deep Learning", "Neural Networks", "Optimization"]
            }
        ],
        
        "projects": [
            {
                "title": "Interpretable Deep Learning Framework",
                "description": "Developed framework for explaining deep neural network predictions. Published at ICML 2023",
                "technologies": ["PyTorch", "Python", "XAI"],
                "link": "https://arxiv.org/pdf/2306.xxxxx.pdf"
            }
        ],
        
        "technical_skills": [
            "Python", "PyTorch", "TensorFlow", "Machine Learning", "Deep Learning",
            "Neural Architecture Search", "Data Science", "Research Methodologies"
        ],
        "soft_skills": [
            "Academic Writing", "Teaching", "Mentoring", "Critical Thinking", "Presentation"
        ],
        "certifications": [
            "Teaching Certificate - Stanford University"
        ],
        "languages": ["English", "Spanish"]
    },
    "style": "academic",
    "tone": "formal"
}


# ============================================================================
# API USAGE FUNCTIONS
# ============================================================================

def generate_resume(profile_data: dict, endpoint: str = "/generate"):
    """
    Generate resume content or PDF
    
    Args:
        profile_data: Complete request payload with student_profile, style, tone
        endpoint: "/generate" for content, "/generate-pdf" for PDF, "/preview" for preview
    """
    try:
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            json=profile_data,
            timeout=30
        )
        
        if response.status_code == 200:
            if endpoint == "/generate-pdf":
                # Save PDF
                filename = f"{profile_data['student_profile']['full_name'].replace(' ', '_')}_resume.pdf"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"✓ PDF saved as: {filename}")
                return filename
            else:
                return response.json()
        else:
            print(f"✗ Error {response.status_code}: {response.text}")
            return None
            
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("AI RESUME GENERATOR - COMPREHENSIVE EXAMPLES")
    print("=" * 70)
    
    # Make sure server is running first!
    print("\nMake sure the server is running:")
    print("  python -m uvicorn ai_backend.main:app --reload\n")
    
    # Example 1: Entry-level engineer resume
    print("\n1. Generating Entry-Level Software Engineer Resume...")
    print("-" * 70)
    result = generate_resume(ENTRY_LEVEL_ENGINEER, "/generate")
    if result and 'data' in result:
        print(f"Professional Summary: {result['data'].get('professional_summary', '')[:100]}...")
    
    # Example 2: Data scientist resume
    print("\n2. Generating Mid-Level Data Scientist Resume...")
    print("-" * 70)
    result = generate_resume(MID_LEVEL_DATA_SCIENTIST, "/generate")
    if result and 'data' in result:
        print(f"Professional Summary: {result['data'].get('professional_summary', '')[:100]}...")
    
    # Example 3: Creative designer resume with creative style
    print("\n3. Generating Creative Designer Resume (Creative Style)...")
    print("-" * 70)
    result = generate_resume(CREATIVE_DESIGNER, "/generate")
    if result and 'data' in result:
        print(f"Professional Summary: {result['data'].get('professional_summary', '')[:100]}...")
    
    # Example 4: Academic researcher resume
    print("\n4. Generating Academic Researcher Resume...")
    print("-" * 70)
    result = generate_resume(ACADEMIC_RESEARCHER, "/generate")
    if result and 'data' in result:
        print(f"Professional Summary: {result['data'].get('professional_summary', '')[:100]}...")
    
    # Example 5: Generate PDF for entry-level engineer
    print("\n5. Generating PDF Resume...")
    print("-" * 70)
    pdf_file = generate_resume(ENTRY_LEVEL_ENGINEER, "/generate-pdf")
    
    print("\n" + "=" * 70)
    print("Examples completed! Check the generated resumes.")
    print("=" * 70)
