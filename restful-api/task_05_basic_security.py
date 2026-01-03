#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
import base64

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "admin": {"username": "admin", "password": "adminpass", "role": "admin"},
    "user": {"username": "user", "password": "userpass", "role": "user"},
}


@jwt.unauthorized_loader
def unauthorized(_err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(_err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token(_jwt_header, _jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


def _parse_basic_auth():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Basic "):
        return None, None

    b64_part = auth.split(" ", 1)[1].strip()
    try:
        decoded = base64.b64decode(b64_part).decode("utf-8")
    except Exception:
        return None, None

    if ":" not in decoded:
        return None, None

    username, password = decoded.split(":", 1)
    return username, password


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or user.get("password") != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"access_token": token}), 200


@app.route("/basic-protected", methods=["GET"])
def basic_protected():
    username, password = _parse_basic_auth()
    if not username:
        return jsonify({"error": "Unauthorized"}), 401

    user = users.get(username)
    if not user or user.get("password") != password:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    user = users.get(username)

    if not user or user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


if __name__ == "__main__":
    app.run()

