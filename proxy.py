from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Proxy credentials (use environment variables for better security)
username = os.getenv('PROXY_USERNAME', 'spwkucrla4')
password = os.getenv('PROXY_PASSWORD', '0Emcdc=J2aqr8Jp4nE')
proxy = f"http://{username}:{password}@dc.smartproxy.com:10000"

@app.route('/fetch_html', methods=['GET'])
def fetch_html():
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "URL parameter is missing!"}), 400

    try:
        # Send GET request through the proxy
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})

        if response.status_code == 200:
            # Return HTML content with correct content-type
            return Response(response.text, status=200, content_type='text/html')
        else:
            return jsonify({"error": f"Failed to fetch URL, status code: {response.status_code}"}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request failed: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the app on the Codespaces default host and port
    app.run(host='0.0.0.0', port=8080)
