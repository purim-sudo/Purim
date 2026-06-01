from flask import Flask, jsonify
import platform
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'project': 'PurimMonitor',
        'status': 'running'
    })

@app.route('/stats')
def stats():
    return jsonify({
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'system': platform.system()
    })

if __name__ == '__main__':
    app.run(debug=True)
