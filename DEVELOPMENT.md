# Development Guide

This file explains how to work with the repository locally.

## Requirements

- Python 3.11 or newer
- Node.js 20 or newer
- Make

## Run all checks

```bash
make test
```

## Python checks

```bash
make test-python
```

## Node.js checks

```bash
make test-node
```

## Project layout

Each project lives in its own folder. Keep changes focused and add tests when behavior changes.

## Good commit style

Use short commit messages that explain the purpose of the change.

Examples:

- Add sample output for LogLens
- Improve PurimMonitor metadata response
- Document SecureShare configuration
