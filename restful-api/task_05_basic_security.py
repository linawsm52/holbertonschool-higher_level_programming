#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash
import base64

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
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


def _get_basic_credentials():
    auth_obj = request.authorization
    if auth_obj and auth_obj.username and auth_obj.password:
        return auth_obj.username, auth_obj.password

    auth = request.headers.get("Authorization", "")
    if not auth:
        return None, None

    parts = auth.split(None, 1)
    if len(parts) != 2 or parts[0].lower() != "basic":
        return None, None

    try:
        decoded = base64.b64decode(parts[1]).decode("utf-8")
    except Exception:
        return None, None

    if ":" not in decoded:
        return None, None

    return decoded.split(":", 1)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"access_token": token}), 200


@app.route("/basic-protected", methods=["GET"])
def basic_protected():
    username, password = _get_basic_credentials()
    if not username:
        return "Unauthorized", 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return "Unauthorized", 401

    return "Basic Auth: Access Granted", 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


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
