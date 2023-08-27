import requests

# Data in a normal python dictionary
data = {"key1": 1, "key2": 2}

# Send data as request body through json parameter
response = requests.post("localhost:8000/testEndpoint", json=data)
