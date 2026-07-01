# Purim Labs

Purim Labs is a portfolio repository of practical backend services, command-line tools, log helpers, and project workflow utilities.

The goal is to show clean structure, useful code, automated tests, sample outputs, and documentation across more than one type of software project.

Start here:

- [SHOWCASE.md](SHOWCASE.md) - short portfolio viewing guide
- [docs/DEMO_GUIDE.md](docs/DEMO_GUIDE.md) - step-by-step demo flow
- [examples/](examples/) - sample inputs and JSON outputs
- [portfolio.json](portfolio.json) - machine-readable project summary
- [DEVELOPMENT.md](DEVELOPMENT.md) - local development guide

## Project Portfolio

| Project | Stack | Purpose | Shows |
| --- | --- | --- | --- |
| [PurimMonitor](PurimMonitor/) | Python, Flask, psutil | Service health API with status, version, uptime, and machine metadata. | API design, monitoring, tests |
| [SecureShare](SecureShare/) | Node.js, Express | Temporary sharing API prototype with route protection, expiring records, and request limits. | Backend structure, API flow, tests |
| [NetWatch](NetWatch/) | Python | Local diagnostic helper with explicit inputs and validation. | CLI design, validation, utilities |
| [LogLens](LogLens/) | Python | Log summary helper with readable and JSON output. | Parsing, summaries, automation |
| [PortalCheck](PortalCheck/) | Python | Local setup-note reviewer for planning and checklist signals. | Text analysis, planning tools |

## Why This Repo Matters

This repository shows a practical engineering mindset beyond one single app:

- Backend API design with Flask and Express
- Command-line tool development
- Testable application and utility functions
- Python and Node.js automated test coverage
- Continuous checks with GitHub Actions
- Clear documentation for each major tool
- Example files for quick review
- A roadmap for turning experiments into stronger products

## Repository Structure

```text
PurimMonitor/   Flask service health API
SecureShare/    Node.js sharing API prototype
NetWatch/       Python diagnostic helper
LogLens/        Python log summary helper
PortalCheck/    Python setup-note reviewer
docs/           Demo and review notes
examples/       Sample inputs and outputs
.github/        GitHub Actions workflow
SHOWCASE.md     Portfolio viewing guide
DEVELOPMENT.md  Local development guide
portfolio.json  Project summary data
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

## Portfolio Talking Points

- Practical tools, not only tutorial-style examples
- Multiple small projects under one consistent engineering theme
- Automated tests and repeatable checks included
- Backend, CLI, documentation, and support-tooling experience
- Sample files make the projects easier to understand quickly
- Clear project roadmap for future growth

## Roadmap

Planned ideas for future commits:

- Uptime alerting service
- Callback testing helper
- Deployment checklist generator
- Simple admin dashboard that links the tools together
- Docker examples for selected services

## Vision

Purim Labs focuses on practical, lightweight software tools for small teams, operations, and self-hosted systems.
