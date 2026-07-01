# Purim Labs

Purim Labs is a practical portfolio of lightweight infrastructure, monitoring, networking, log analysis, and secure API experiments.

The repository is designed around small tools that can be useful for VPS administration, support workflows, hotspot-style deployments, and self-hosted systems.

## Project Portfolio

| Project | Stack | Purpose |
| --- | --- | --- |
| [PurimMonitor](PurimMonitor/) | Python, Flask, psutil | Server health API with CPU, memory, disk, system, hostname, and health endpoints. |
| [SecureShare](SecureShare/) | Node.js, Express | Temporary file-sharing API prototype with protected routes, expiring records, rate limits, and security headers. |
| [NetWatch](NetWatch/) | Python | Local network diagnostics with explicit host/port inputs and subnet hostname discovery. |
| [LogLens](LogLens/) | Python | HTTP and application log analyzer with readable summaries and JSON output. |
| [PortalCheck](PortalCheck/) | Python | Local setup-note reviewer for portal, branding, billing, and deployment checklist signals. |

## Why This Repo Matters

This repository shows a full-stack engineering mindset beyond one single app:

- Backend API design with Flask and Express
- CLI tooling for infrastructure and support workflows
- Security-aware defaults and protected API routes
- Testable application factories and utility functions
- Python and Node.js automated test coverage
- CI workflow for repeatable validation
- Clear project documentation for each major tool

## Repository Structure

```text
PurimMonitor/   Flask-based server monitoring API
SecureShare/    Node.js secure file-sharing API prototype
NetWatch/       Python network diagnostic utilities
LogLens/        Python log analysis CLI
PortalCheck/    Python local setup checklist reviewer
.github/        GitHub Actions workflow
```

## Quick Start

Run all tests:

```bash
make test
```

Run Python tests only:

```bash
make test-python
```

Run Node.js tests only:

```bash
make test-node
```

## Individual Test Commands

```bash
PYTHONPATH=PurimMonitor python -m unittest discover -s PurimMonitor/tests
PYTHONPATH=NetWatch python -m unittest discover -s NetWatch/tests
PYTHONPATH=LogLens python -m unittest discover -s LogLens/tests
PYTHONPATH=PortalCheck python -m unittest discover -s PortalCheck/tests
cd SecureShare && npm ci && npm test
```

## Current Focus Areas

- Infrastructure health checks
- API reliability and security basics
- Local network support utilities
- Log troubleshooting and operational summaries
- Portal and billing workflow preparation

## Roadmap

Planned ideas for future commits:

- Uptime alerting service
- MPESA callback testing helper
- eTIMS sandbox helper utilities
- Deployment checklist generator
- Simple admin dashboard that links the tools together
- Docker Compose examples for selected services

## Vision

Purim Labs focuses on practical, lightweight tooling for small businesses, hotspot environments, and self-hosted systems.
