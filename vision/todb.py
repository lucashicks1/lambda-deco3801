import requests
import json

users = ["Timmy", "Kimmy", "Jimmy", "Timmy_Jr", "family"]

for user in users:
    with open(f'./premade/{user}.json', 'r') as request_body:
        request_body = json.loads(request_body.read())
        request_body = {"body": request_body}
        requests.post(f"http://127.0.0.1:8000/whiteboard/{user}", json=request_body, timeout=30)
