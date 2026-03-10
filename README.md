# AI Resume Generator

A FastAPI-based backend service that generates AI-powered resumes using Groq API.

## Features

- **AI-Powered Resume Generation**: Uses Groq's Llama 3.1 8B model to generate compelling professional summaries and experience highlights
- **PDF Generation**: Converts generated resumes to professional PDF format
- **Multiple Resume Styles**: Support for professional, creative, and academic styles
- **Streaming Response**: Leverages Groq's streaming API for faster response times
- **Flexible Input**: Accepts student profiles with education, experience, projects, and skills
- **Resume Preview**: Preview the formatted resume before PDF generation

## Project Structure

```
ai_backend/
├── __init__.py
├── main.py                  # FastAPI application entry point
├── config.py                # Configuration management
├── routes/
│   ├── __init__.py
│   ├── chat.py             # Chat endpoint (legacy)
│   └── resume.py           # Resume generation endpoints
├── schemas/
│   ├── __init__.py
│   ├── chat_schema.py      # Chat request/response models
│   └── resume_schema.py    # Student profile and resume models
└── services/
    ├── __init__.py
    ├── llm_service.py      # Legacy LLM service
    ├── resume_service.py   # Resume generation logic
    └── pdf_service.py      # PDF generation logic
```

## Installation

1. **Clone the repository** (or navigate to the project folder)

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your Groq API key
   ```

   Get your Groq API key from: https://console.groq.com

## Configuration

Edit `.env` file with your settings:

```env
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
GROQ_TEMPERATURE=1.0
GROQ_MAX_TOKENS=1024
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

## Running the Server

Start the FastAPI development server:

```bash
python -m uvicorn ai_backend.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

API Documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### 1. Generate Resume Content
**POST** `/api/resume/generate`

Generate resume content using AI without creating a PDF.

**Request Body**:
```json
{
  "student_profile": {
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-234-567-8900",
    "location": "San Francisco, CA",
    "education": [
      {
        "institution": "UC Berkeley",
        "degree": "Bachelor of Science",
        "field": "Computer Science",
        "graduation_year": 2021,
        "gpa": 3.8
      }
    ],
    "experiences": [
      {
        "company": "Tech Corp",
        "position": "Engineer",
        "duration": "2021-Present",
        "description": "Developing software",
        "skills": ["Python", "FastAPI"]
      }
    ],
    "technical_skills": ["Python", "JavaScript", "FastAPI"],
    "soft_skills": ["Leadership", "Communication"],
    "certifications": ["AWS Certified"],
    "languages": ["English", "Spanish"]
  },
  "style": "professional",
  "tone": "formal"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Resume generated successfully",
  "data": {
    "professional_summary": "...",
    "formatted_experience": "...",
    "formatted_skills": "...",
    "formatted_education": "...",
    "additional_sections": "..."
  }
}
```

### 2. Generate PDF Resume
**POST** `/api/resume/generate-pdf`

Generate resume and return as downloadable PDF file.

**Same request body as above**

**Response**: PDF file download

### 3. Preview Resume
**POST** `/api/resume/preview`

Preview the formatted resume content without generating PDF.

**Same request body as above**

**Response**:
```json
{
  "success": true,
  "message": "Resume preview generated successfully",
  "content": "Formatted resume text...",
  "metadata": {
    "name": "John Doe",
    "email": "john@example.com",
    "style": "professional",
    "tone": "formal"
  }
}
```

### 4. Health Check
**GET** `/`

Check if the API is running.

## Usage Examples

### Using Python
```python
import requests

profile = {
    "full_name": "Jane Smith",
    "email": "jane@example.com",
    "education": [...],
    "experiences": [...],
    "technical_skills": [...]
}

response = requests.post(
    "http://localhost:8000/api/resume/generate-pdf",
    json={
        "student_profile": profile,
        "style": "professional",
        "tone": "formal"
    }
)

with open("resume.pdf", "wb") as f:
    f.write(response.content)
```

### Using cURL
```bash
curl -X POST "http://localhost:8000/api/resume/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "student_profile": {
      "full_name": "John Doe",
      "email": "john@example.com",
      ...
    },
    "style": "professional",
    "tone": "formal"
  }'
```

## Resume Styles

- **professional**: Formal, business-focused resume suitable for corporate roles
- **creative**: More dynamic, highlights personality and unique strengths
- **academic**: Emphasizes education and research contributions

## Resume Tones

- **formal**: Professional business language
- **casual**: Conversational, friendly language
- **friendly**: Approachable and warm tone

## Generated Resume Sections

1. **Professional Summary**: AI-generated 2-3 sentence summary highlighting key strengths
2. **Professional Experience**: Work history with AI-enhanced bullet points
3. **Skills**: Technical and soft skills organized by category
4. **Education**: Academic background with GPA if available
5. **Projects**: Notable projects with technologies used
6. **Certifications**: Professional certifications and credentials
7. **Languages**: Professional language proficiencies

## Dependencies

- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI web server
- **Pydantic**: Data validation and serialization
- **Groq**: Groq API client for LLM access
- **ReportLab**: PDF generation library
- **python-dotenv**: Environment variable management

## Error Handling

The API returns appropriate HTTP status codes:

- `200`: Success
- `400`: Bad request (invalid input)
- `500`: Server error (includes error message)

All errors include descriptive messages to help with debugging.

## Logging

Logs are configured based on the `LOG_LEVEL` environment variable (default: `INFO`).

View logs for debugging and monitoring:
```bash
# Run with debug logging
LOG_LEVEL=DEBUG python -m uvicorn ai_backend.main:app --reload
```

## Performance Notes

- **Streaming**: Groq's streaming API is used for faster response times
- **Token Limits**: Default max tokens set to 1024, configurable via `GROQ_MAX_TOKENS`
- **Temperature**: Set to 1.0 for more creative responses (configurable)

## Troubleshooting

### API Key Error
- Ensure `GROQ_API_KEY` is set in `.env` file
- Get your key from https://console.groq.com
- Verify the key is valid and has active quota

### PDF Generation Issues
- Ensure `reportlab` is installed
- Check that the `resumes/` directory exists (created automatically)
- Verify sufficient disk space for PDF storage

### Connection Errors
- Verify the server is running
- Check host and port in `.env` match your curl/request
- Ensure firewall isn't blocking the port

## Future Enhancements

- Database integration for storing generated resumes
- User authentication and authorization
- Resume templates and themes
- Resume analytics and version control
- Email integration for sending resumes
- Support for additional file formats (DOCX, HTML)
- Resume ATS optimization

## License

MIT License

## Support

For issues and questions, please refer to the Groq documentation:
- https://console.groq.com/docs

## Contributors

AI Resume Generator Team
