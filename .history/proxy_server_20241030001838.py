from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# CORS headers to allow requests from your Amplify app URL
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://master.djeji3xcqctxi.amplifyapp.com'  # Change to your Amplify URL
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Define your route for login and any other API calls that need proxying
@app.route('/api/method/login', methods=['POST'])
def proxy_login():
    # Your Frappe API URL
    frappe_url = 'https://portal.somasiriafrika.tech/api/method/login'
    
    # Get the data from the incoming request
    data = request.json

    try:
        # Make a POST request to the Frappe server
        response = requests.post(frappe_url, json=data, headers={'Content-Type': 'application/json'})

        # Return the response from Frappe as JSON
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Handle other routes similarly
@app.route('/api/resource/User', methods=['GET'])
def get_user_details():
    frappe_url = 'https://portal.somasiriafrika.tech/api/resource/User'
    
    try:
        # Make a GET request to the Frappe server
        response = requests.get(frappe_url, headers={'Content-Type': 'application/json'})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost with a custom port
    app.run(host='0.0.0.0', port=5000, debug=True)
