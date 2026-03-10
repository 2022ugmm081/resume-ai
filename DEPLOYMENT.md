# AI Resume Generator - Deployment Guide

## Local Development

For development and testing:

```bash
# Activate virtual environment
venv\Scripts\activate

# Run with auto-reload
python -m uvicorn ai_backend.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker Deployment

### Prerequisites
- Docker installed
- Docker Compose installed

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t ai-resume-generator .

# Run the container
docker run -p 8000:8000 \
  -e GROQ_API_KEY=your_api_key \
  -v $(pwd)/resumes:/app/resumes \
  ai-resume-generator
```

### Using Docker Compose (Recommended)

```bash
# Create .env file with your API key
echo "GROQ_API_KEY=your_api_key_here" > .env

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f ai_resume_api

# Stop services
docker-compose down
```

## Cloud Deployment Options

### Option 1: Heroku Deployment

#### Prerequisites
- Heroku CLI installed
- Git repository initialized

#### Deployment Steps

1. **Create Heroku app**:
   ```bash
   heroku create ai-resume-generator
   ```

2. **Set environment variables**:
   ```bash
   heroku config:set GROQ_API_KEY=your_api_key
   heroku config:set PORT=8000
   ```

3. **Create Procfile**:
   ```
   web: python -m uvicorn ai_backend.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Create runtime.txt**:
   ```
   python-3.10.13
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

6. **View logs**:
   ```bash
   heroku logs --tail
   ```

### Option 2: AWS Deployment

#### Using AWS App Runner (Simplest)

1. **Push code to GitHub**
2. **In AWS Console**:
   - Go to App Runner
   - Create service → GitHub source
   - Select repository and branch
   - Configure environment variables:
     - `GROQ_API_KEY`
     - `PORT=8000`

3. **AWS handles deployment automatically**

#### Using EC2

1. **Launch EC2 instance** (Ubuntu 20.04)

2. **SSH into instance**:
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install dependencies**:
   ```bash
   sudo apt update
   sudo apt install -y python3-pip python3-venv git
   ```

4. **Clone repository**:
   ```bash
   git clone your-repo-url
   cd ai_resume_saas
   ```

5. **Setup Python environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Create systemd service**:
   ```bash
   sudo nano /etc/systemd/system/ai-resume.service
   ```

   Add:
   ```ini
   [Unit]
   Description=AI Resume Generator API
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/ai_resume_saas
   Environment="PATH=/home/ubuntu/ai_resume_saas/venv/bin"
   Environment="GROQ_API_KEY=your_api_key"
   ExecStart=/home/ubuntu/ai_resume_saas/venv/bin/python -m uvicorn ai_backend.main:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

7. **Start service**:
   ```bash
   sudo systemctl start ai-resume
   sudo systemctl enable ai-resume
   ```

8. **Configure Nginx reverse proxy**:
   ```bash
   sudo apt install -y nginx
   ```

   Create `/etc/nginx/sites-available/ai-resume`:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

   Enable:
   ```bash
   sudo ln -s /etc/nginx/sites-available/ai-resume /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### Option 3: Google Cloud Run

1. **Create `cloudbuild.yaml`**:
   ```yaml
   steps:
     - name: 'gcr.io/cloud-builders/docker'
       args: ['build', '-t', 'gcr.io/$PROJECT_ID/ai-resume-generator', '.']
     - name: 'gcr.io/cloud-builders/docker'
       args: ['push', 'gcr.io/$PROJECT_ID/ai-resume-generator']
   images:
     - 'gcr.io/$PROJECT_ID/ai-resume-generator'
   ```

2. **Deploy**:
   ```bash
   gcloud run deploy ai-resume-generator \
     --image=gcr.io/YOUR_PROJECT_ID/ai-resume-generator \
     --set-env-vars=GROQ_API_KEY=your_api_key \
     --memory=1Gi \
     --timeout=3600 \
     --region=us-central1
   ```

### Option 4: DigitalOcean App Platform

1. Push code to GitHub
2. In DigitalOcean:
   - Go to App Platform
   - New App → GitHub
   - Select repository
   - Configure:
     - Build command: Leave empty
     - Run command: `python -m uvicorn ai_backend.main:app --host 0.0.0.0 --port 8080`
     - Environment variables: Add `GROQ_API_KEY`

## Production Considerations

### Security

1. **Never commit API keys**:
   - Use environment variables
   - Add `.env` to `.gitignore`

2. **Enable HTTPS**:
   - Use SSL/TLS certificates
   - Let's Encrypt (free) or Cloudflare

3. **API Rate Limiting**:
   ```python
   from fastapi_limiter import FastAPILimiter
   from fastapi_limiter.util import get_remote_address
   
   @app.post("/api/resume/generate")
   @limiter.limit("5/minute")
   async def generate_resume(request: ResumeGenerationRequest):
       ...
   ```

4. **CORS Configuration**:
   - Restrict allowed origins in `config.py`
   - Don't allow "*" in production

### Performance

1. **Use production ASGI server**:
   ```bash
   pip install gunicorn
   gunicorn ai_backend.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. **Enable caching**:
   - Cache resume templates
   - Cache API responses where appropriate

3. **Monitor API usage**:
   - Track Groq API calls
   - Monitor response times
   - Log errors

### Scaling

1. **Horizontal Scaling**:
   - Use load balancer
   - Run multiple instances

2. **Database**:
   - Add PostgreSQL for user data
   - Store resume history

3. **Background Jobs**:
   - Use Celery for long-running PDF generation
   - Process async with Redis queue

## Monitoring & Logging

### Application Logging

```python
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
```

### Health Checks

The app has built-in health check:
```
GET /health
```

Configure monitoring tools to hit this endpoint.

### Error Tracking

For production, integrate error tracking:

```bash
pip install sentry-sdk
```

```python
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FastApiIntegration()]
)
```

## Maintenance

### Updating Dependencies

```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade groq

# Update all
pip install --upgrade -r requirements.txt
```

### Backup

1. **Database backup** (if using database):
   ```bash
   pg_dump your_db > backup.sql
   ```

2. **Generated resumes**: Store in cloud storage (S3, GCS)

## Troubleshooting Deployment

### Issue: 502 Bad Gateway
- Check if application is running
- Look at logs: `docker logs container_id`
- Verify Groq API key

### Issue: Timeout errors
- Increase timeout settings
- Check Groq API status
- Monitor network connectivity

### Issue: High memory usage
- Reduce worker count
- Monitor PDF generation memory
- Consider async processing

## Cost Optimization

1. **Groq API**: Monitor token usage
2. **Storage**: Use cloud storage for PDFs
3. **Compute**: Start small, scale as needed
4. **CDN**: Serve PDFs via CDN for faster delivery

## Quick Reference

| Platform | Cost | Setup Time | Scaling |
|----------|------|-----------|---------|
| Heroku | $7-50/mo | 5 min | Easy |
| AWS App Runner | $0.065/hour | 10 min | Auto |
| Google Cloud Run | Pay per use | 15 min | Auto |
| DigitalOcean | $6/mo | 5 min | Manual |
| EC2 | $5-100/mo | 30 min | Manual |

---

Choose the deployment option that best fits your needs, budget, and scalability requirements!
