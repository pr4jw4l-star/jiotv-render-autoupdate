
from flask import Flask, Response, request
import base64
import subprocess

USERNAME = "Prajwal_07"
PASSWORD = "prajwal@521112"

app = Flask(__name__)

def check_auth(auth_header):
    if not auth_header or not auth_header.startswith("Basic "):
        return False
    encoded = auth_header.split(" ")[1]
    decoded = base64.b64decode(encoded).decode("utf-8")
    username, password = decoded.split(":", 1)
    return username == USERNAME and password == PASSWORD

@app.route("/")
def index():
    auth = request.headers.get("Authorization")
    if not check_auth(auth):
        return Response("Unauthorized", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})

    try:
        result = subprocess.run(["python", "jioTV.py"], capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return Response("Failed to generate playlist", status=500)
        return Response(result.stdout, mimetype="application/x-mpegURL")
    except Exception as e:
        return Response(f"Error: {e}", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
