# Setup Guide

## PurimMonitor

```bash
cd PurimMonitor
pip install -r requirements.txt
python app.py
```

For production-style local execution:

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## SecureShare

```bash
cd SecureShare
npm install
JWT_SECRET=change-this-secret-to-at-least-32-characters npm start
```

For Docker Compose, copy `.env.example` to `.env` and set a unique `JWT_SECRET`.

## NetWatch

```bash
cd NetWatch
python scanner.py --host 127.0.0.1 --ports 22,80,443
python subnet_scan.py 192.168.1.0/24 --limit 20
```

Only scan networks you own or are authorized to test.
