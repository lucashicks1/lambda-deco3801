import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/whiteboard/user_4', headers = headers, json={
    "body": [
        {
            "day": "tuesday",
            "time_slot": 12,
            "data": "minecraft gaming"
        }
    ]
})

print(r.json())
