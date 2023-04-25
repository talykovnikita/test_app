# from app.data import NT
import json as json_module
from flask import Flask
from flask import jsonify, make_response, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    response = dict(
        status='Is working!',
        request_method=request.method,
        request_headers=dict(request.headers)
    )
    return make_response(jsonify(response), 200)


@app.route("/not-found-page", methods=["GET", "POST"])
def not_found():
    response = dict(
        status='Not found!',
        request_method=request.method,
        request_headers=dict(request.headers)
    )
    return make_response(jsonify(response), 404)


@app.route("/internal-error-page", methods=["GET"])
def internal_error():
    response = dict(
        status='Not found!',
        request_method=request.method,
        request_headers=dict(request.headers)
    )

    return make_response(jsonify(response), 500)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() in ["true", "yes"]
    host = os.environ.get("HOST", "")

    app.run(debug=debug, host=host, port=port)
