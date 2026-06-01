# Purim Labs

A collection of infrastructure, monitoring, networking, and security-focused experimental projects.

## Projects

### PurimMonitor
A Python Flask dashboard for monitoring VPS and server infrastructure.

Features:
- CPU and RAM monitoring
- uptime tracking
- API health checks
- system statistics dashboard
- production WSGI deployment with Gunicorn

### SecureShare
A secure file-sharing platform prototype focused on temporary encrypted sharing.

Features:
- expiring file links
- upload management
- encrypted-ready architecture
- secure download endpoints
- JWT-protected API endpoints
- request rate limiting and security headers

### NetWatch
A lightweight network monitoring and LAN scanning utility.

Features:
- local network scanning
- ping monitoring
- device discovery
- port status checking
- explicit CLI arguments for safe, targeted scans

## Stack
- Python
- Flask
- Node.js
- HTML/CSS/JavaScript

## Test

```bash
PYTHONPATH=PurimMonitor python -m unittest discover -s PurimMonitor/tests
PYTHONPATH=NetWatch python -m unittest discover -s NetWatch/tests
cd SecureShare && npm test
```

Or run everything with:

```bash
make test
```

## Vision
Purim Labs focuses on lightweight infrastructure and security tooling for small businesses, hotspot environments, and self-hosted systems.
