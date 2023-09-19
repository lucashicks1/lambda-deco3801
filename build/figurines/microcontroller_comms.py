import serial.tools.list_ports
import threading
import time
from time import sleep
import requests
import socket

figurine_status = {}
response = {}
POLL_DELAY = 15

global connect_status, read_state, port, serialPort
global serial_count  # Optimized counter, used to clear the serial input buffer
serial_count = 0
connect_status = False  # Serial connection state
read_state = True  # True when serial starts up connection

# =========================== Serial Parsing ==================================


def initialise_serial(port):
    global serialPort, connect_status
    print("PRC [Starting Serial at " + port + "]")
    serialPort = serial.Serial(port, baudrate=9600,
                              bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)
    connect_status = True  # Set the connection status to True when serial is initialized


def serial_disconnect():
    global serialPort, connect_status
    serialPort.flushInput()
    serialPort.flushOutput()
    serialPort.close()
    connect_status = False  # Set the connection status to False when serial is disconnected


def serial_send_data(data):
    global read_state, serialPort
    read_state = False  # Pause Reading serial
    print("Sending " + str(data))
    serialPort.write(data)
    read_state = True  # Resume Reading serial


def serial_read_data(serialPort):
    global serial_count
    serialString = serialPort.readline()
    serial_count += 1
    if serial_count == 20:
        serialPort.reset_input_buffer()
        serialPort.flush()
        serial_count = 0

# =========================== ESP32 Wifi Parsing ================================


def connect_to_esp32(esp32_ip, esp32_port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the ESP32
        client_socket.connect((esp32_ip, esp32_port))
        print(f"Connected to {esp32_ip}:{esp32_port}")

        while True:
            message = input("Enter a message to send (or 'exit' to quit): ")

            # Send the message to the ESP32
            client_socket.sendall(message.encode())

            if message.lower() == 'exit':
                break

        # Close the socket
        client_socket.close()
    except Exception as e:
        print(f"Connection failed: {e}")

# =========================== Threading Stuff ==================================


def check_presence(port, interval=0.01):
    while True:
        time.sleep(interval)
        if not connect_status:
            print("THR [Stopping Thread at port:", port, "]")
            print("Status Thread [stopped]")
            print("PRC [Stopping Serial]")
            serial_disconnect()
            break

        if read_state:
            serial_read_data(serialPort)  # Pass serialPort as a parameter


def start_thread():
    global port, connect_status
    print("THR [Starting Thread at port:", port, "]")
    port_controller = threading.Thread(target=check_presence, args=(port, 0.1))
    port_controller.setDaemon(True)
    port_controller.start()


def send_to_controller(value):
    com_string = "".join(str(value[key]) for key in sorted(value))
    data = bytes("FIG" + com_string, 'utf-8')
    serial_send_data(data)

def main():
    global port, connect_status

    while True:
        if not connect_status:
            port = serial.tools.list_ports.comports()
            coms = [com[0] for com in port]
            if coms:
                initialise_serial(coms[0])
                start_thread()
            else:
                connect_status = False
            continue
        if serialPort.is_open:
            try:
                print("Polling now")
                send_to_controller({"family": 0, "user_1":0, "user_2":0, "user_3":0, "user_4":0})
                sleep(POLL_DELAY)
                send_to_controller({"family": 0, "user_1":1, "user_2":0, "user_3":0, "user_4":0})
                sleep(POLL_DELAY)
                send_to_controller({"family": 0, "user_1":1, "user_2":1, "user_3":1, "user_4":0})
                sleep(POLL_DELAY)
                send_to_controller({"family": 0, "user_1":0, "user_2":1, "user_3":1, "user_4":0})
                sleep(POLL_DELAY)
                send_to_controller({"family": 1, "user_1":0, "user_2":0, "user_3":0, "user_4":0})
                sleep(POLL_DELAY)
            except Exception as e:
                serial_disconnect()
                print(f"Error connecting to serial: {e}")

if __name__ == "__main__":
    main()
