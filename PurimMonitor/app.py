import os
import platform
import sys
import time

import psutil
from flask import Flask, jsonify


VERSION = "1.1.0"


def get_load_average():
    if hasattr(os, "getloadavg"):
        return tuple(round(value, 2) for value in os.getloadavg())
    return None


def collect_system_stats():
    boot_time = psutil.boot_time()

    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "system": platform.system(),
        "release": platform.release(),
        "hostname": platform.node(),
        "python_version": platform.python_version(),
        "boot_time_unix": int(boot_time),
        "uptime_seconds": max(0, int(time.time() - boot_time)),
        "load_average": get_load_average(),
    }


def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        return response

    @app.route("/")
    def home():
        return jsonify(
            {
                "project": "PurimMonitor",
                "status": "running",
                "version": VERSION,
                "runtime": "python",
            }
        )

    @app.route("/stats")
    def stats():
        return jsonify(collect_system_stats())

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy", "version": VERSION})

    @app.route("/version")
    def version():
        return jsonify(
            {
                "project": "PurimMonitor",
                "version": VERSION,
                "python_version": sys.version.split()[0],
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    host = os.getenv("HOST", "127.0.0.1")
    app.run(host=host, port=port, debug=os.getenv("FLASK_DEBUG") == "1")
