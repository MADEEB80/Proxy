import requests

# Proxy configuration
proxies = {
    "http": "http://9cb7911bc7dce412c1bd__cr.us:e3d1e6433ed3da7c@gw.dataimpulse.com:823",
    "https": "http://9cb7911bc7dce412c1bd__cr.us:e3d1e6433ed3da7c@gw.dataimpulse.com:823"
}

# Target URL
url = "https://api.ipify.org/"

try:
    # Fetch the URL using the proxy
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # Raise an error for bad HTTP responses
    
    # Save the result to a file
    with open("resultpage.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("The result has been saved to resultpage.html.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

