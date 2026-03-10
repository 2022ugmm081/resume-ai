"""
Quick Start Guide for AI Resume Generator

This script helps you quickly test the AI Resume Generator API.
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"


def test_health_check():
    """Test if the API is running"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print("✓ Health check passed")
        print(f"  Response: {response.json()}\n")
        return True
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to API. Make sure the server is running:")
        print("  python -m uvicorn ai_backend.main:app --reload\n")
        return False


def test_simple_resume():
    """Test with a simple student profile"""
    simple_profile = {
        "full_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "+1-555-123-4567",
        "location": "New York, NY",
        
        "education": [
            {
                "institution": "NYU - Stern School of Business",
                "degree": "Bachelor of Science",
                "field": "Data Science",
                "graduation_year": 2023,
                "gpa": 3.9
            }
        ],
        
        "experiences": [
            {
                "company": "DataCorp Analytics",
                "position": "Data Analyst",
                "duration": "2023 - Present",
                "description": "Analyze datasets and create data visualizations for stakeholders. Built dashboards using Python and Tableau.",
                "skills": ["Python", "SQL", "Tableau", "Excel"]
            }
        ],
        
        "technical_skills": ["Python", "SQL", "Tableau", "Excel", "Power BI"],
        "soft_skills": ["Communication", "Analytical Thinking", "Problem Solving"],
        "certifications": ["Google Analytics Certified"],
        "languages": ["English", "French"]
    }
    
    payload = {
        "student_profile": simple_profile,
        "style": "professional",
        "tone": "formal"
    }
    
    try:
        print("Sending request to generate resume...")
        response = requests.post(
            f"{BASE_URL}/api/resume/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✓ Resume generated successfully!\n")
            print("Generated Content Preview:")
            print("-" * 70)
            
            data = result.get('data', {})
            if data.get('professional_summary'):
                print(f"Professional Summary:\n{data['professional_summary']}\n")
            
            if data.get('formatted_experience'):
                print(f"Experience Highlights:\n{data['formatted_experience']}\n")
            
            return True
        else:
            print(f"✗ Error: {response.status_code}")
            print(f"  Response: {response.text}\n")
            return False
            
    except requests.exceptions.Timeout:
        print("✗ Request timed out. The AI generation may be taking longer.")
        print("  This is normal for the first request. Please try again.\n")
        return False
    except Exception as e:
        print(f"✗ Error: {str(e)}\n")
        return False


def test_pdf_generation():
    """Test PDF generation"""
    simple_profile = {
        "full_name": "John Developer",
        "email": "john.dev@example.com",
        "location": "San Francisco, CA",
        
        "education": [
            {
                "institution": "Stanford University",
                "degree": "Bachelor of Science",
                "field": "Computer Science",
                "graduation_year": 2022,
                "gpa": 3.7
            }
        ],
        
        "experiences": [
            {
                "company": "Tech Startup",
                "position": "Full Stack Developer",
                "duration": "2022 - Present",
                "description": "Developed web applications using React and Node.js",
                "skills": ["JavaScript", "React", "Node.js"]
            }
        ],
        
        "technical_skills": ["JavaScript", "React", "Node.js", "MongoDB"],
        "soft_skills": ["Teamwork", "Communication"]
    }
    
    payload = {
        "student_profile": simple_profile,
        "style": "professional",
        "tone": "formal"
    }
    
    try:
        print("Generating PDF resume...")
        response = requests.post(
            f"{BASE_URL}/api/resume/generate-pdf",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            filename = "test_resume.pdf"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"✓ PDF generated successfully!")
            print(f"  Saved as: {filename}\n")
            return True
        else:
            print(f"✗ Error: {response.status_code}")
            print(f"  Response: {response.text}\n")
            return False
            
    except requests.exceptions.Timeout:
        print("✗ Request timed out during PDF generation.\n")
        return False
    except Exception as e:
        print(f"✗ Error: {str(e)}\n")
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("AI RESUME GENERATOR - QUICK START TEST")
    print("=" * 70 + "\n")
    
    # Test 1: Health check
    print("Test 1: Checking API Health...\n")
    if not test_health_check():
        return
    
    # Test 2: Simple resume generation
    print("Test 2: Generating Resume with AI...\n")
    time.sleep(1)
    if not test_simple_resume():
        print("Note: If you're seeing a timeout error, it might be the first request.")
        print("Groq may take a bit longer to initialize. Please try again.\n")
    
    # Test 3: PDF generation
    print("\nTest 3: Generating PDF Resume...\n")
    time.sleep(2)
    test_pdf_generation()
    
    print("=" * 70)
    print("TESTS COMPLETED")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Check the generated PDF file if it was created")
    print("2. Review the example_usage.py file for more examples")
    print("3. Read the README.md for API documentation")
    print("4. Customize the student profile with real data")
    print("\nAPI Documentation available at:")
    print("  http://localhost:8000/docs (Swagger UI)")
    print("  http://localhost:8000/redoc (ReDoc)\n")


if __name__ == "__main__":
    main()
