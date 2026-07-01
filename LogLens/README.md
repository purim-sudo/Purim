# LogLens

LogLens is a lightweight Python CLI for quickly summarizing HTTP access logs and plain application logs.

It is useful when checking small VPS deployments, API services, hotspot portals, reverse proxies, or self-hosted tools where you want a fast operational overview without installing a full observability stack.

## Features

- Parses common HTTP access log lines
- Counts HTTP statuses, methods, and top paths
- Detects application log levels such as `INFO`, `WARNING`, `ERROR`, and `CRITICAL`
- Captures a small sample of error lines for quick triage
- Supports readable terminal output and JSON output for automation
- Uses only the Python standard library

## Usage

```bash
python LogLens/loglens.py /var/log/nginx/access.log
```

JSON output:

```bash
python LogLens/loglens.py /var/log/nginx/access.log --json
```

Limit top results:

```bash
python LogLens/loglens.py app.log --top 10
```

## Example Output

```text
LogLens Summary
===============
Total lines: 1200
HTTP requests: 1100
Text events: 100
HTTP status counts: {'200': 980, '404': 80, '500': 40}
HTTP methods: {'GET': 900, 'POST': 200}
Top paths: {'/': 400, '/health': 250, '/login': 120}
Log levels: {'INFO': 80, 'ERROR': 20}
```

## Test

```bash
PYTHONPATH=LogLens python -m unittest discover -s LogLens/tests
```
