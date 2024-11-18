from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Proxy configuration
PROXIES = {
    "http": "http://9cb7911bc7dce412c1bd__cr.us:e3d1e6433ed3da7c@gw.dataimpulse.com:823",
    "https": "http://9cb7911bc7dce412c1bd__cr.us:e3d1e6433ed3da7c@gw.dataimpulse.com:823"
}

@app.route("/fetch", methods=["POST"])
def fetch_url():
    try:
        data = request.json
        url = data.get("url")
        
        if not url:
            return jsonify({"error": "URL is required"}), 400
        
        # Fetch the URL using the proxy
        response = requests.get(url, proxies=PROXIES)
        response.raise_for_status()
        
        # Return the HTML content
        return jsonify({"html": response.text})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
