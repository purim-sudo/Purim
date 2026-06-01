const crypto = require('crypto');
const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');

const { authenticate, getJwtSecret } = require('./auth');

const VERSION = '1.0.0';
const DEFAULT_UPLOAD_TTL_SECONDS = 3600;
const DEFAULT_MAX_UPLOADS = 1000;

function parsePositiveInteger(value, fallback) {
  const parsed = Number.parseInt(value, 10);
  return Number.isInteger(parsed) && parsed > 0 ? parsed : fallback;
}

function createUploadStore(options = {}) {
  const ttlSeconds = parsePositiveInteger(options.ttlSeconds, DEFAULT_UPLOAD_TTL_SECONDS);
  const maxUploads = parsePositiveInteger(options.maxUploads, DEFAULT_MAX_UPLOADS);
  const uploads = new Map();

  function expiresAtFrom(now) {
    return new Date(now.getTime() + ttlSeconds * 1000);
  }

  function pruneExpired(now = new Date()) {
    for (const [id, upload] of uploads) {
      if (upload.expires_at <= now) {
        uploads.delete(id);
      }
    }
  }

  function create(metadata = {}, now = new Date()) {
    pruneExpired(now);

    if (uploads.size >= maxUploads) {
      const oldestId = uploads.keys().next().value;
      uploads.delete(oldestId);
    }

    const id = crypto.randomUUID();
    const upload = {
      id,
      name: metadata.name || null,
      size: metadata.size || null,
      created_at: now,
      expires_at: expiresAtFrom(now),
    };

    uploads.set(id, upload);
    return upload;
  }

  function list(now = new Date()) {
    pruneExpired(now);
    return Array.from(uploads.values());
  }

  function get(id, now = new Date()) {
    pruneExpired(now);
    return uploads.get(id) || null;
  }

  return { create, list, get, pruneExpired };
}

function createApp(options = {}) {
  const app = express();
  const store = options.store || createUploadStore({
    ttlSeconds: process.env.UPLOAD_TTL_SECONDS,
    maxUploads: process.env.MAX_UPLOADS,
  });

  app.disable('x-powered-by');
  app.use(helmet());
  app.use(express.json({ limit: process.env.JSON_BODY_LIMIT || '100kb' }));

  if (process.env.NODE_ENV !== 'test') {
    app.use(morgan('combined'));
  }

  app.use(rateLimit({
    windowMs: 60 * 1000,
    limit: parsePositiveInteger(process.env.RATE_LIMIT_PER_MINUTE, 60),
    standardHeaders: true,
    legacyHeaders: false,
  }));

  app.get('/', (req, res) => {
    res.json({
      project: 'SecureShare',
      status: 'online',
      version: VERSION,
    });
  });

  app.get('/health', (req, res) => {
    res.json({ status: 'healthy' });
  });

  app.post('/upload', authenticate, (req, res) => {
    const { name = null, size = null } = req.body || {};

    if (name !== null && (typeof name !== 'string' || name.length > 255)) {
      return res.status(400).json({ error: 'name must be a string up to 255 characters' });
    }

    if (size !== null && (!Number.isInteger(size) || size < 0)) {
      return res.status(400).json({ error: 'size must be a non-negative integer' });
    }

    const upload = store.create({ name, size });

    return res.status(201).json({
      message: 'Upload registered',
      file_id: upload.id,
      expires_at: upload.expires_at.toISOString(),
    });
  });

  app.get('/files', authenticate, (req, res) => {
    res.json(store.list().map((upload) => ({
      id: upload.id,
      name: upload.name,
      size: upload.size,
      created_at: upload.created_at.toISOString(),
      expires_at: upload.expires_at.toISOString(),
    })));
  });

  app.get('/files/:id', authenticate, (req, res) => {
    const upload = store.get(req.params.id);

    if (!upload) {
      return res.status(404).json({ error: 'File not found' });
    }

    return res.json({
      id: upload.id,
      name: upload.name,
      size: upload.size,
      created_at: upload.created_at.toISOString(),
      expires_at: upload.expires_at.toISOString(),
    });
  });

  return app;
}

if (require.main === module) {
  const port = parsePositiveInteger(process.env.PORT, 3000);
  getJwtSecret();

  const app = createApp();

  app.listen(port, () => {
    console.log(`SecureShare running on port ${port}`);
  });
}

module.exports = { createApp, createUploadStore, parsePositiveInteger };
