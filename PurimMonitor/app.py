import os
import platform

import psutil
from flask import Flask, jsonify


VERSION = "1.0.0"


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
            }
        )

    @app.route("/stats")
    def stats():
        return jsonify(
            {
                "cpu_percent": psutil.cpu_percent(interval=None),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage("/").percent,
                "system": platform.system(),
                "hostname": platform.node(),
            }
        )

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"})

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_DEBUG") == "1")
