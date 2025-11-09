from flask import request, redirect, url_for, jsonify

def init_routes(app):
    @app.route("/login", methods=["POST"])
    def api_login():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if username == "admin" and password == "secret":
            return {"token": "fake-jwt-token"}, 200
        else:
            return {"error": "Invalid credentials"}, 401

    @app.route("/success/<name>")
    def success(name):
        return f"welcome {name}"
