from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Basic route for the root URL
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Proxy server is running!"})

# Example of a proxy route for login (you can customize this as needed)
@app.route("/proxy/login", methods=["POST"])
def proxy_login():
    data = request.get_json()
    api_url = "https://portal.somasiriafrika.tech/api/method/login"

    try:
        response = requests.post(api_url, json=data, headers={
            "Content-Type": "application/json",
            # Include other necessary headers if required
        })

        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
