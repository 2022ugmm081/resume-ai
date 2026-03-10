# AI Resume Generator - Setup Guide

## Prerequisites

- Python 3.8 or higher
- Groq API account (free)
- pip or conda package manager

## Step 1: Get Groq API Key

1. Visit https://console.groq.com
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy the key (you'll need this in Step 3)

## Step 2: Install Dependencies

### Option A: Using pip

```bash
# Navigate to the project directory
cd d:\Projects\ai_resume_saas

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option B: Using conda

```bash
# Create conda environment
conda create -n resume-generator python=3.10
conda activate resume-generator

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables

1. Copy the example environment file:
```bash
copy .env.example .env
# On macOS/Linux:
cp .env.example .env
```

2. Open `.env` file and add your Groq API key:
```env
GROQ_API_KEY=your_actual_api_key_here
```

3. Save the file

## Step 4: Run the Server

```bash
# Make sure you're in the project directory
cd d:\Projects\ai_resume_saas

# Ensure virtual environment is activated
venv\Scripts\activate

# Start the FastAPI server
python -m uvicorn ai_backend.main:app --reload --host 0.0.0.0 --port 8000
```

You should see output like:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [12345]
```

## Step 5: Test the API

In a new terminal window, run the test script:

```bash
# Activate virtual environment
venv\Scripts\activate

# Run tests
python test_api.py
```

This will:
- Check if the API is running
- Test resume generation with AI
- Test PDF generation

## Step 6: Access API Documentation

Once the server is running, open your browser:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Common Tasks

### Generate a Resume Programmatically

```python
import requests

profile = {
    "full_name": "John Doe",
    "email": "john@example.com",
    "technical_skills": ["Python", "FastAPI"],
    "education": [{
        "institution": "University",
        "degree": "BS",
        "field": "Computer Science",
        "graduation_year": 2023
    }]
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
      "technical_skills": ["Python"],
      "education": [{
        "institution": "University",
        "degree": "BS",
        "field": "CS",
        "graduation_year": 2023
      }]
    },
    "style": "professional",
    "tone": "formal"
  }'
```

## Troubleshooting

### Issue: "GROQ_API_KEY not found"
**Solution**: Make sure `.env` file exists in the project root and contains your API key

### Issue: "ModuleNotFoundError: No module named 'groq'"
**Solution**: 
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

### Issue: "Connection refused" when accessing API
**Solution**:
- Make sure server is running (`python -m uvicorn ai_backend.main:app --reload`)
- Check that port 8000 is available (no other app using it)

### Issue: Timeout errors when generating resume
**Solution**: 
- This is normal for first request as Groq initializes
- Try again, it will be faster
- Check internet connection
- Verify Groq API key is valid

### Issue: Permission denied error
**Solution**: 
- Ensure you have write permissions in the project directory
- The app creates a `resumes/` folder for storing PDFs

## Project Structure

```
ai_resume_saas/
├── ai_backend/               # Main backend package
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Configuration settings
│   ├── routes/
│   │   ├── chat.py          # Chat endpoints (legacy)
│   │   └── resume.py        # Resume generation endpoints
│   ├── schemas/
│   │   ├── chat_schema.py   # Chat data models
│   │   └── resume_schema.py # Resume data models
│   └── services/
│       ├── llm_service.py   # LLM integration (legacy)
│       ├── resume_service.py # Resume generation logic
│       └── pdf_service.py   # PDF generation logic
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment variables
├── README.md               # Full documentation
├── SETUP.md               # This file
├── test_api.py            # Quick test script
├── example_usage.py       # Usage examples
└── resumes/               # Generated PDFs (auto-created)
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `GROQ_API_KEY` | - | Your Groq API key (required) |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | Model to use for generation |
| `GROQ_TEMPERATURE` | `1.0` | Creativity level (0-2) |
| `GROQ_MAX_TOKENS` | `1024` | Max tokens per response |
| `DEBUG` | `False` | Enable debug mode |
| `PORT` | `8000` | Server port |
| `HOST` | `0.0.0.0` | Server host |
| `PDF_STORAGE_PATH` | `resumes` | Directory for storing PDFs |
| `RESUME_DEFAULT_STYLE` | `professional` | Default resume style |
| `LOG_LEVEL` | `INFO` | Logging level |

## Next Steps

1. **Customize the resume generation**: Edit `ai_backend/services/resume_service.py`
2. **Add database support**: Integrate with a database to store user profiles
3. **Add authentication**: Implement user login and profile management
4. **Deploy**: Deploy to cloud services (Heroku, AWS, Google Cloud, etc.)
5. **Add frontend**: Create a web interface for resume generation
6. **Add more features**: Resume templates, version control, analytics

## Support & Resources

- **Groq Documentation**: https://console.groq.com/docs
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **ReportLab Documentation**: https://www.reportlab.com/docs/reportlab-userguide.pdf

## Tips

- For production, use HTTPS and secure API keys
- Consider adding rate limiting to prevent abuse
- Monitor API usage and token consumption
- Keep dependencies updated: `pip install --upgrade -r requirements.txt`
- Use a production ASGI server like Gunicorn instead of uvicorn for deployment

Good luck with your AI Resume Generator! 🚀
