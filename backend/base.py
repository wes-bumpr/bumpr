from flask import Flask, jsonify
from flask_cors import CORS

api = Flask(__name__)
CORS(api, origins="*")  # Enable CORS for all routes


@api.route("/profile")
def my_profile():
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
    }

    return jsonify(response_body)
