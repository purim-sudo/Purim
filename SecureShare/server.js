const express = require('express');
const crypto = require('crypto');
const app = express();

app.use(express.json());

const uploads = [];

app.get('/', (req, res) => {
  res.json({
    project: 'SecureShare',
    status: 'online',
    version: '1.0.0'
  });
});

app.post('/upload', (req, res) => {
  const id = crypto.randomUUID();

  uploads.push({
    id,
    created: new Date()
  });

  res.json({
    message: 'Upload registered',
    file_id: id
  });
});

app.get('/files', (req, res) => {
  res.json(uploads);
});

app.listen(3000, () => {
  console.log('SecureShare running on port 3000');
});
