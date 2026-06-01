const assert = require('node:assert/strict');
const http = require('node:http');
const test = require('node:test');

const { generateToken } = require('../auth');
const { createApp, createUploadStore, parsePositiveInteger } = require('../server');

function request(server, method, path, body, token) {
  const payload = body === undefined ? null : JSON.stringify(body);
  const address = server.address();

  return new Promise((resolve, reject) => {
    const req = http.request({
      hostname: '127.0.0.1',
      port: address.port,
      path,
      method,
      headers: {
        ...(payload ? { 'content-type': 'application/json', 'content-length': Buffer.byteLength(payload) } : {}),
        ...(token ? { authorization: `Bearer ${token}` } : {}),
      },
    }, (res) => {
      let data = '';

      res.setEncoding('utf8');
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          body: data ? JSON.parse(data) : null,
        });
      });
    });

    req.on('error', reject);

    if (payload) {
      req.write(payload);
    }

    req.end();
  });
}

async function withServer(app, callback) {
  const server = http.createServer(app);

  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));

  try {
    await callback(server);
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
}

test('parsePositiveInteger falls back for unsafe values', () => {
  assert.equal(parsePositiveInteger('10', 1), 10);
  assert.equal(parsePositiveInteger('0', 1), 1);
  assert.equal(parsePositiveInteger('abc', 1), 1);
});

test('health and root endpoints are public', async () => {
  await withServer(createApp(), async (server) => {
    const home = await request(server, 'GET', '/');
    const health = await request(server, 'GET', '/health');

    assert.equal(home.statusCode, 200);
    assert.equal(home.body.project, 'SecureShare');
    assert.equal(health.statusCode, 200);
    assert.deepEqual(health.body, { status: 'healthy' });
    assert.equal(home.headers['x-powered-by'], undefined);
  });
});

test('upload endpoints require a bearer token', async () => {
  await withServer(createApp(), async (server) => {
    const response = await request(server, 'POST', '/upload', { name: 'report.pdf' });

    assert.equal(response.statusCode, 401);
  });
});

test('authenticated uploads can be listed and fetched', async () => {
  const token = generateToken({ sub: 'test-user' });

  await withServer(createApp(), async (server) => {
    const upload = await request(server, 'POST', '/upload', { name: 'report.pdf', size: 42 }, token);

    assert.equal(upload.statusCode, 201);
    assert.match(upload.body.file_id, /^[0-9a-f-]{36}$/);

    const files = await request(server, 'GET', '/files', undefined, token);
    assert.equal(files.statusCode, 200);
    assert.equal(files.body.length, 1);
    assert.equal(files.body[0].name, 'report.pdf');

    const file = await request(server, 'GET', `/files/${upload.body.file_id}`, undefined, token);
    assert.equal(file.statusCode, 200);
    assert.equal(file.body.size, 42);
  });
});

test('upload store prunes expired records', () => {
  const store = createUploadStore({ ttlSeconds: 1, maxUploads: 10 });
  const now = new Date('2026-01-01T00:00:00.000Z');

  store.create({ name: 'temporary.txt' }, now);
  assert.equal(store.list(now).length, 1);
  assert.equal(store.list(new Date('2026-01-01T00:00:02.000Z')).length, 0);
});
