from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to enable cross-origin requests
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default

# Basic route for the root URL
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Proxy server is running!"})

# Example of a proxy route for login
@app.route("/proxy/login", methods=["POST"])
def proxy_login():
    data = request.get_json()
    api_url = "https://portal.somasiriafrika.tech/api/method/login"

    try:
        # Forward the received headers (e.g., authorization) if needed
        headers = {
            "Content-Type": "application/json",
        }
        # Add any authorization headers received from the frontend
        if "Authorization" in request.headers:
            headers["Authorization"] = request.headers["Authorization"]

        response = requests.post(api_url, json=data, headers=headers)

        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Remove debug mode for production
    app.run(host="0.0.0.0", port=5000)
