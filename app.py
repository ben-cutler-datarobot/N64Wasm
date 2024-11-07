import logging
import os

from flask import Flask, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

logger = logging.getLogger(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)
@app.route("/")
def index_route():
    return send_from_directory('.', 'index.html')


@app.route('/<path:filename>')
def serve_static_file(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)