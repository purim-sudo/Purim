const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.json({
    project: 'SecureShare',
    status: 'online'
  });
});

app.post('/upload', (req, res) => {
  res.json({
    message: 'Upload endpoint initialized'
  });
});

app.listen(3000, () => {
  console.log('SecureShare running on port 3000');
});
