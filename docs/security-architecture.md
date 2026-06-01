# Security Architecture

## SecureShare
- JWT authentication with an environment-provided secret in production
- Protected upload and file metadata endpoints
- Rate limiting and hardened HTTP headers
- Expiring upload metadata
- Planned encrypted uploads

## PurimMonitor
- Health monitoring
- Infrastructure visibility
- Hardened response headers
- Non-debug production container command
- Planned authentication layer

## NetWatch
- Internal network diagnostics
- Explicit host, port, subnet, and limit controls
- Import-safe modules for testability
- Planned device fingerprinting
