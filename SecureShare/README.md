# SecureShare

SecureShare is a lightweight API prototype for temporary file-sharing workflows.

It focuses on clean API structure, protected routes, expiring upload records, simple configuration, and testable Express application design.

## Features

- Temporary upload metadata
- Expiring file records
- Protected API routes
- Request limits
- Security headers
- Test-friendly app factory

## Stack

- Node.js
- Express
- JSON Web Tokens
- Helmet
- express-rate-limit

## API

Public routes:

- `GET /`
- `GET /health`

Protected routes:

- `POST /upload`
- `GET /files`
- `GET /files/:id`

## Configuration

An example configuration file is provided at `.env.example`.

Useful settings include:

- `PORT`
- `JWT_SECRET`
- `JWT_EXPIRES_IN`
- `UPLOAD_TTL_SECONDS`
- `MAX_UPLOADS`
- `RATE_LIMIT_PER_MINUTE`
- `JSON_BODY_LIMIT`

## Run

```bash
npm ci
npm start
```

## Test

```bash
npm ci
npm test
```
