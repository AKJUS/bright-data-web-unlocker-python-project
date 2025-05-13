import requests

headers = {
    # Step 1: Get your API token here: https://brightdata.com/cp/setting/users
    "Authorization": "Bearer BRIGHT_DATA_API_TOKEN",
    "Content-Type": "application/json"
}
data = {
    # Step 2: Get your zone here: https://brightdata.com/cp/zones 
    "zone": "web_unlocker1", 
    # Step 3: Set your target URL
    "url": "https://geo.brdtest.com/welcome.txt", 
    # Step 4: Run `python index.py` commend on terminal
    "format": "raw"
}

# Make request to Bright Data Web Unlocker API
url = "https://api.brightdata.com/request"

response = requests.post(url, json=data, headers=headers)
print(response.text)