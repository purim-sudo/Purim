const jwt = require('jsonwebtoken');

const SECRET = 'purim-secret-key';

function authenticate(req, res, next) {
  const authHeader = req.headers['authorization'];
  if (!authHeader) return res.status(401).json({ error: 'No token' });

  const token = authHeader.split(' ')[1];

  jwt.verify(token, SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}

function generateToken(user) {
  return jwt.sign(user, SECRET, { expiresIn: '1h' });
}

module.exports = { authenticate, generateToken };
