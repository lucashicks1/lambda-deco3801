import serial
import serial.tools.list_ports
import threading
import time
from time import sleep
import requests
import socket

figurine_status = {}
response = {}
POLL_DELAY = 15

global connect_status, read_state, port
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


def serial_disconnect():
    serialPort.flushInput()
    serialPort.flushOutput()
    serialPort.close()


def serial_send_data(data):
    global read_state, serialPort
    read_state = False  # Pause Reading serial
    print("Sending " + str(data))
    serialPort.write(data)
    read_state = True  # Resume Reading serial


def serial_read_data():
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
        if connect_status is False:
            print("THR [Stopping Thread at port:", port, "]")
            print("Status Thread [stopped]")
            print("PRC [Stopping Serial]")
            serial_disconnect()
            break

        if read_state is True:
            serial_read_data()


def start_thread():
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
                connect_status = True
                start_thread()
                initialise_serial(coms[0])
            else:
                connect_status = False
            continue
        if serialPort.isOpen():
            try:
                print("Polling now")
                response = requests.get("http://127.0.0.1:8000/figurines")
                
                if response.text == figurine_status:
                    print("No change to figure state")
                else:
                    print("Change to figure status")
                    figurine_status = response.text
                    print("Current figure status: " + figurine_status)
                    send_to_controller(figurine_status)
                    
                sleep(POLL_DELAY)
            except Exception as e:
                serial_disconnect()
                connect_status = False
                print(f"Error connecting to serial: {e}")

if __name__ == "__main__":
    main()






    
