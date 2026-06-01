const jwt = require('jsonwebtoken');

const DEVELOPMENT_SECRET = 'development-only-secret-change-me';

function getJwtSecret() {
  const secret = process.env.JWT_SECRET;

  if (secret && secret.length >= 32) {
    return secret;
  }

  if (process.env.NODE_ENV === 'production') {
    throw new Error('JWT_SECRET must be set to at least 32 characters in production');
  }

  return DEVELOPMENT_SECRET;
}

function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing bearer token' });
  }

  const token = authHeader.slice('Bearer '.length);

  return jwt.verify(token, getJwtSecret(), (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid token' });
    }

    req.user = user;
    return next();
  });
}

function generateToken(user) {
  return jwt.sign(user, getJwtSecret(), { expiresIn: process.env.JWT_EXPIRES_IN || '1h' });
}

module.exports = { authenticate, generateToken, getJwtSecret };
