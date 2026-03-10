# AI Resume Generator - Quick Reference Guide

## 🚀 Quick Start (5 minutes)

### 1. Get Groq API Key
- Visit https://console.groq.com
- Sign up/login → API Keys → Create new key
- Copy the key

### 2. Setup Project
```bash
cd d:\Projects\ai_resume_saas
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
# Create .env file in project root
copy .env.example .env

# Edit .env and add your Groq API key:
# GROQ_API_KEY=your_actual_key_here
```

### 4. Run Server
```bash
python -m uvicorn ai_backend.main:app --reload
```

### 5. Test API
In another terminal:
```bash
python test_api.py
```

**Done! API is running at http://localhost:8000** ✅

---

## 📚 API Endpoints

### 1. Generate Resume Content
```
POST /api/resume/generate
```
Returns: JSON with generated resume sections

### 2. Generate PDF Resume
```
POST /api/resume/generate-pdf
```
Returns: PDF file download

### 3. Preview Resume
```
POST /api/resume/preview
```
Returns: Formatted text preview

### 4. Health Check
```
GET /
GET /health
```

---

## 📋 Example Request

```bash
curl -X POST "http://localhost:8000/api/resume/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "student_profile": {
      "full_name": "John Doe",
      "email": "john@example.com",
      "technical_skills": ["Python", "FastAPI"],
      "education": [{
        "institution": "University",
        "degree": "BS",
        "field": "Computer Science",
        "graduation_year": 2023
      }]
    },
    "style": "professional",
    "tone": "formal"
  }'
```

---

## 🐍 Python Usage

```python
import requests

profile = {
    "full_name": "Jane Doe",
    "email": "jane@email.com",
    "technical_skills": ["Python"],
    "education": [{
        "institution": "University",
        "degree": "BS",
        "field": "CS",
        "graduation_year": 2023
    }]
}

# Generate PDF
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

---

## 📁 Project Structure

```
ai_resume_saas/
├── ai_backend/
│   ├── main.py              ← FastAPI app
│   ├── config.py            ← Settings
│   ├── routes/
│   │   ├── resume.py        ← Resume endpoints
│   │   └── chat.py
│   ├── schemas/
│   │   └── resume_schema.py ← Data models
│   └── services/
│       ├── resume_service.py ← Generation logic
│       └── pdf_service.py    ← PDF creation
├── requirements.txt         ← Dependencies
├── .env.example            ← Environment template
├── .env                    ← Your config (git ignored)
├── README.md               ← Full documentation
├── SETUP.md                ← Installation guide
├── DEPLOYMENT.md           ← Cloud deployment
└── resumes/                ← Generated PDFs
```

---

## ⚙️ Configuration

### Environment Variables (.env)
```env
GROQ_API_KEY=your_key_here           # Required
GROQ_MODEL=llama-3.1-8b-instant      # Default: llama-3.1-8b-instant
GROQ_TEMPERATURE=1.0                 # Default: 1.0 (0-2)
GROQ_MAX_TOKENS=1024                 # Default: 1024
PORT=8000                            # Default: 8000
DEBUG=False                          # Default: False
LOG_LEVEL=INFO                       # Default: INFO
```

---

## 🎨 Resume Styles & Tones

### Styles
- **professional**: Corporate, formal, business-focused
- **creative**: Dynamic, personality-driven, unique
- **academic**: Research-focused, education-emphasis

### Tones
- **formal**: Professional business language
- **casual**: Conversational, friendly
- **friendly**: Approachable, warm

---

## 🧪 Testing

### Run Full Test Suite
```bash
python test_api.py
```

### Run Comprehensive Examples
```bash
python comprehensive_examples.py
```

### Run Single Example
```bash
python example_usage.py
```

---

## 🐳 Docker (Optional)

### Build & Run
```bash
docker build -t ai-resume-generator .
docker run -p 8000:8000 -e GROQ_API_KEY=your_key ai-resume-generator
```

### Using Docker Compose
```bash
docker-compose up -d
```

---

## 📖 API Documentation

Once server is running:
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| ImportError: No module 'groq' | `pip install -r requirements.txt` |
| GROQ_API_KEY not found | Create `.env` file with your key |
| Connection refused | Make sure server is running with uvicorn |
| Timeout error | Normal for first request; try again |
| Permission denied | Run terminal as admin or check directory permissions |

---

## 📦 Dependencies

- **fastapi==0.104.1** - Web framework
- **uvicorn[standard]==0.24.0** - ASGI server
- **pydantic==2.5.0** - Data validation
- **groq==0.4.2** - Groq API client
- **reportlab==4.0.7** - PDF generation
- **python-dotenv==1.0.0** - Environment variables

---

## 🔗 Useful Links

- **Groq Console**: https://console.groq.com
- **Groq Documentation**: https://console.groq.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Python 3.10**: https://www.python.org/downloads/

---

## 💡 Common Tasks

### Change Default Resume Style
Edit `config.py`:
```python
RESUME_DEFAULT_STYLE: str = "creative"  # or "academic"
```

### Increase Max Tokens
Edit `.env`:
```env
GROQ_MAX_TOKENS=2048
```

### Enable Debug Mode
Edit `.env`:
```env
DEBUG=True
LOG_LEVEL=DEBUG
```

### Change Server Port
Edit `.env`:
```env
PORT=8080
```

---

## 📞 Support

- **Issues**: Check SETUP.md or DEPLOYMENT.md
- **API Questions**: See README.md
- **Groq Issues**: https://console.groq.com/docs
- **FastAPI Issues**: https://fastapi.tiangolo.com/

---

## ✨ What You Can Do

✅ Generate AI-powered resumes from student profiles
✅ Create multiple resume styles (professional, creative, academic)
✅ Export as PDF files
✅ Preview resume content before PDF generation
✅ Handle streaming responses for faster generation
✅ Deploy to cloud (Heroku, AWS, Google Cloud, etc.)
✅ Integrate with databases
✅ Add authentication and user management

---

## 🚀 Next Steps

1. ✅ **Setup** - Follow Quick Start above
2. 📝 **Customize** - Edit student profiles in `comprehensive_examples.py`
3. 🧪 **Test** - Run `test_api.py`
4. 🚀 **Deploy** - Follow `DEPLOYMENT.md`
5. 🔧 **Extend** - Add features (database, auth, etc.)

---

**Happy Resume Generating! 🎉**
