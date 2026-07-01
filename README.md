# Purim Labs

Purim Labs is a collection of lightweight infrastructure, monitoring, networking, log analysis, and security-focused experimental tools.

The goal is to build practical utilities for small businesses, VPS environments, hotspot deployments, and self-hosted systems.

## Projects

| Project | Stack | Purpose |
| --- | --- | --- |
| [PurimMonitor](PurimMonitor/) | Python, Flask, psutil | VPS/server health dashboard with CPU, RAM, disk, uptime, and API health checks. |
| [SecureShare](SecureShare/) | Node.js, Express, JWT | Secure temporary file-sharing API prototype with expiring upload records and protected endpoints. |
| [NetWatch](NetWatch/) | Python | Local network diagnostics, safe port checks, and subnet hostname discovery. |
| [LogLens](LogLens/) | Python | HTTP/application log analyzer with terminal and JSON summaries. |

## Highlights

- Small tools that can run on low-cost VPS infrastructure
- Clear CLI/API boundaries
- Security-conscious defaults where applicable
- Unit tests for Python and Node.js projects
- GitHub Actions CI for automated checks
- No heavy dependencies for utility-style projects such as NetWatch and LogLens

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
cd SecureShare && npm ci && npm test
```

## Project Ideas Roadmap

Potential future additions:

- MikroTik hotspot diagnostics helper
- Small uptime alerting service
- Lightweight MPESA/Daraja callback tester
- eTIMS integration sandbox utilities
- Nginx and firewall configuration audit scripts

## Vision

Purim Labs focuses on practical, lightweight infrastructure and security tooling for small businesses, hotspot environments, and self-hosted systems.
