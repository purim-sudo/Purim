from flask import Flask, jsonify
import platform
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'project': 'PurimMonitor',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/stats')
def stats():
    return jsonify({
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'system': platform.system(),
        'hostname': platform.node()
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy'
    })

if __name__ == '__main__':
    app.run(debug=True)
