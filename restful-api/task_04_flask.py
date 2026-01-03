#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK", 200


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.values())), 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    data_json = request.get_json(silent=True)

    if data_json is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data_json.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data_json
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()

