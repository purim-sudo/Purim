# SecureShare

SecureShare is a lightweight secure file-sharing prototype.

## Planned Features
- Temporary file links
- Encryption-ready architecture
- Upload expiration
- Authentication support
- Download tracking

## Stack
- Node.js
- Express

## Configuration

Set `JWT_SECRET` to at least 32 characters in production.

Optional environment variables:
- `PORT`, default `3000`
- `UPLOAD_TTL_SECONDS`, default `3600`
- `MAX_UPLOADS`, default `1000`
- `RATE_LIMIT_PER_MINUTE`, default `60`
- `JSON_BODY_LIMIT`, default `100kb`

## API

Public:
- `GET /`
- `GET /health`

Authenticated with `Authorization: Bearer <token>`:
- `POST /upload`
- `GET /files`
- `GET /files/:id`

## Test

```bash
npm install
npm test
```
