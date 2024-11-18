from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Proxy credentials
username = 'spwkucrla4'
password = '0Emcdc=J2aqr8Jp4nE'
proxy = f"http://{username}:{password}@dc.smartproxy.com:10000"

@app.route('/fetch_html', methods=['GET'])
def fetch_html():
    # Get the URL from the request parameter
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "URL parameter is missing!"}), 400
    
    try:
        # Send GET request through the proxy
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        
        # Check if request was successful
        if response.status_code == 200:
            # Return the HTML content as a response
            return response.text, 200
        else:
            return jsonify({"error": f"Failed to fetch URL, status code: {response.status_code}"}), response.status_code
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the app on the Codespaces default host and port
    app.run(host='0.0.0.0', port=8080)
