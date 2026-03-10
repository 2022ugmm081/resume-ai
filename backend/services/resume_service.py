from groq import Groq
from schemas.resume_schema import StudentProfile, ResumeContent
import json
import logging

logger = logging.getLogger(__name__)

client = Groq()


def generate_professional_summary(profile: StudentProfile, style: str = "professional", tone: str = "formal") -> str:
    """
    Generate a professional summary using Groq with streaming
    """
    prompt = f"""Based on the following student profile, generate a compelling professional summary for a resume.
    
Student Name: {profile.full_name}
Email: {profile.email}
Location: {profile.location}
Technical Skills: {', '.join(profile.technical_skills)}
Soft Skills: {', '.join(profile.soft_skills)}
Education: {profile.education[0].degree if profile.education else 'Not specified'}
Experience Level: {len(profile.experiences)} years if {len(profile.experiences) > 0 else 'Entry-level'}

Style: {style}
Tone: {tone}

Generate a 2-3 sentence professional summary that highlights key strengths and career goals. Be concise and impactful."""

    response_text = ""
    
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_completion_tokens=500,
        top_p=1,
        stream=True,
        stop=None
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
    
    return response_text.strip()


def format_experience(profile: StudentProfile) -> str:
    """
    Format work experience section
    """
    if not profile.experiences:
        return ""
    
    formatted = "PROFESSIONAL EXPERIENCE\n" + "=" * 50 + "\n\n"
    
    for exp in profile.experiences:
        formatted += f"{exp.position}\n"
        formatted += f"{exp.company} | {exp.duration}\n"
        formatted += f"{exp.description}\n"
        if exp.skills:
            formatted += f"Skills: {', '.join(exp.skills)}\n"
        formatted += "\n"
    
    return formatted


def generate_experience_highlights(profile: StudentProfile, style: str = "professional") -> str:
    """
    Generate bullet points for experiences using Groq
    """
    if not profile.experiences:
        return ""
    
    experiences_text = "\n".join([
        f"- {exp.company}: {exp.position} ({exp.duration}) - {exp.description}"
        for exp in profile.experiences
    ])
    
    prompt = f"""Transform the following work experiences into compelling bullet points for a resume. 
Make each point start with a strong action verb and highlight impact/achievements.

Experiences:
{experiences_text}

Generate 2-3 outstanding bullet points for each experience that would impress recruiters."""

    response_text = ""
    
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_completion_tokens=800,
        top_p=1,
        stream=True,
        stop=None
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
    
    return response_text.strip()


def format_skills(profile: StudentProfile) -> str:
    """
    Format skills section
    """
    formatted = "SKILLS\n" + "=" * 50 + "\n\n"
    
    if profile.technical_skills:
        formatted += f"Technical Skills: {', '.join(profile.technical_skills)}\n"
    
    if profile.soft_skills:
        formatted += f"Soft Skills: {', '.join(profile.soft_skills)}\n"
    
    if profile.languages:
        formatted += f"Languages: {', '.join(profile.languages)}\n"
    
    formatted += "\n"
    return formatted


def format_education(profile: StudentProfile) -> str:
    """
    Format education section
    """
    if not profile.education:
        return ""
    
    formatted = "EDUCATION\n" + "=" * 50 + "\n\n"
    
    for edu in profile.education:
        formatted += f"{edu.degree} in {edu.field}\n"
        formatted += f"{edu.institution} | {edu.graduation_year}\n"
        if edu.gpa:
            formatted += f"GPA: {edu.gpa}\n"
        formatted += "\n"
    
    return formatted


def format_projects(profile: StudentProfile) -> str:
    """
    Format projects section
    """
    if not profile.projects:
        return ""
    
    formatted = "PROJECTS\n" + "=" * 50 + "\n\n"
    
    for project in profile.projects:
        formatted += f"{project.title}\n"
        formatted += f"Technologies: {', '.join(project.technologies)}\n"
        formatted += f"{project.description}\n"
        if project.link:
            formatted += f"Link: {project.link}\n"
        formatted += "\n"
    
    return formatted


def format_certifications(profile: StudentProfile) -> str:
    """
    Format certifications section
    """
    if not profile.certifications:
        return ""
    
    formatted = "CERTIFICATIONS\n" + "=" * 50 + "\n\n"
    formatted += "\n".join([f"• {cert}" for cert in profile.certifications])
    formatted += "\n\n"
    
    return formatted


def generate_complete_resume(profile: StudentProfile, style: str = "professional", tone: str = "formal") -> ResumeContent:
    """
    Generate complete resume content using Groq
    """
    
    # Generate professional summary
    professional_summary = generate_professional_summary(profile, style, tone)
    
    # Format structured sections
    formatted_education = format_education(profile)
    formatted_skills = format_skills(profile)
    
    # Generate experience highlights
    formatted_experience = generate_experience_highlights(profile, style)
    
    # Format optional sections
    additional_sections = format_projects(profile) + format_certifications(profile)
    
    return ResumeContent(
        professional_summary=professional_summary,
        formatted_experience=formatted_experience,
        formatted_skills=formatted_skills,
        formatted_education=formatted_education,
        additional_sections=additional_sections if additional_sections else None
    )


def format_resume_for_pdf(profile: StudentProfile, content: ResumeContent) -> str:
    """
    Format resume content for PDF generation
    """
    resume_text = f"""{'=' * 70}
{profile.full_name.upper()}
{'=' * 70}

Email: {profile.email}
{f'Phone: {profile.phone}' if profile.phone else ''}
{f'Location: {profile.location}' if profile.location else ''}

{'=' * 70}
PROFESSIONAL SUMMARY
{'=' * 70}

{content.professional_summary}

{'=' * 70}
PROFESSIONAL EXPERIENCE
{'=' * 70}

{content.formatted_experience}

{'=' * 70}
SKILLS
{'=' * 70}

{content.formatted_skills}

{'=' * 70}
EDUCATION
{'=' * 70}

{content.formatted_education}

"""
    
    if content.additional_sections:
        resume_text += f"""{'=' * 70}
ADDITIONAL INFORMATION
{'=' * 70}

{content.additional_sections}
"""
    
    return resume_text
