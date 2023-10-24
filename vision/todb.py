import requests
import json

USER_NAME = "Timmy"

with open('coloured_time_slots.json', 'r') as request_body:
    request_body = json.loads(request_body.read())
    request_body = {"body": request_body}

    print(request_body)
    requests.post(f"http://127.0.0.1:8000/whiteboard/{USER_NAME}", json=request_body, timeout=30)
