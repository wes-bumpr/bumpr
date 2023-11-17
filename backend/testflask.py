import requests
import json
from flask import request

# Define the Flask API endpoint
# url = "http://localhost:8848/ride-request"  # Update the URL if your Flask app is running on a different address or port
url = "http://localhost:8848"
def test():
    json_data = {"key": "value"}

    # Set the Content-Type header to indicate that you're sending JSON data
    headers = {'Content-Type': 'application/json'}

    # Convert the dictionary to a JSON-formatted string
    json_payload = json.dumps(json_data)

    # Send a POST request with the JSON payload and headers
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # If the response status code is 200, the request was successful.
        print("Request successful.")
        print(response.json())  # Parse the JSON response
    else:
        # If the response status code is not 200, there was an error.
        print("Request failed with status code:", response.status_code)
        print(response.text)

