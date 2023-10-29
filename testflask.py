import requests
import json
import handle_requests

# Define the Flask API endpoint
url = "http://localhost:8848/ride-request"  # Update the URL if your Flask app is running on a different address or port

# Sample JSON data
rideRequestsList = [
    {
        "user_ID": "12345",
        "other_field": "other_value"
    },
    {
        "user_ID": "67890",
        "other_field": "another_value"
    }
]

print("start handle request")
# Send a POST request with the JSON data
response = requests.post(url, json=rideRequestsList)
print("done handling request")

# Check the response
if response.status_code == 200:
    print("Request successful")
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)
