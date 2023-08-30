import requests
from time import sleep
import serial

figurine_status = {}
response = {}
POLL_DELAY = 15

def send_to_display(figurine_status: dict):
    print(figurine_status)

def main():
    while True:
        print("Polling now")
        response = requests.get("http://127.0.0.1:8000/figurines")
        if response.text == figurine_status:
            print("NO CHANGE")
        else:
            print("IT CHANGED!!!!")
            figurine_status = response.text
            print(figurine_status)
            send_to_display(figurine_status)
            # Do pyserial stuff
        # Sleep for 15 seconds
        sleep(POLL_DELAY)

if __name__ == "__main__":
    main()