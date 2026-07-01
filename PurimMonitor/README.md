# PurimMonitor

PurimMonitor is a lightweight Flask service for checking basic VPS and server health.

It exposes simple JSON endpoints that can be used by dashboards, uptime monitors, admin panels, or deployment smoke tests.

## Features

- Root service metadata endpoint
- Health endpoint for uptime checks
- CPU, memory, and disk usage reporting
- Hostname and operating system visibility
- Basic security headers
- Flask application factory for testing and deployment

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Service metadata and current status. |
| `GET` | `/health` | Basic health check response. |
| `GET` | `/stats` | CPU, memory, disk, OS, and hostname statistics. |

## Local Development

```bash
cd PurimMonitor
pip install -r requirements.txt
python app.py
```

By default, the app runs on port `5000` unless the `PORT` environment variable is set.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `PORT` | `5000` | Local development server port. |
| `FLASK_DEBUG` | disabled | Set to `1` to enable debug mode during development. |

## Test

```bash
PYTHONPATH=PurimMonitor python -m unittest discover -s PurimMonitor/tests
```
