# Deployment Guide

## Docker Deployment

```bash
export JWT_SECRET=change-this-secret-to-at-least-32-characters
docker compose up --build
```

## PurimMonitor
Runs on port 5000 with Gunicorn and a `/health` endpoint.

## SecureShare
Runs on port 3000. `JWT_SECRET` is required and must be at least 32 characters in production.

Useful environment variables:
- `UPLOAD_TTL_SECONDS`
- `MAX_UPLOADS`
- `RATE_LIMIT_PER_MINUTE`

## Recommended Future Additions
- HTTPS certificates
- Database persistence
- Object storage for uploaded file bytes
- Centralized logging and metrics
