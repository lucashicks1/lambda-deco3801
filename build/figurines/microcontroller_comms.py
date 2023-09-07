import serial
import serial.tools.list_ports
import threading
import time
from pymongo import MongoClient
import requests
import sockets

figurine_status = {}
response = {}
POLL_DELAY = 15

global connect_status, read_state 
global serial_count # Optimised counter, used to clear the serial input buffer
serial_count = 0
connect_status = False # Serial connection state
read_state = True # True when serial starts up connection


# =========================== Serial Parsing ==================================
def initialise_serial(port):
    global serialPort, connect_status
    print("PRC [Starting Serial at " + port +"]")
    serialPort = serial.Serial(port, baudrate=115200, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)

def serial_disconnect():
    serialPort.flushInput()
    serialPort.flushOutput()
    serialPort.close()

def serial_send_data(data):
    global read_state, serialPort
    read_state = False # Pause Reading serial
    print("Sending "+ str(data))
    serialPort.write(data) #bytes(data, 'UTF-8')
    read_state = True # Resume Reading serial 

def serial_read_data():
    global serial_count
    #time.sleep(0.1)
    serialString = serialPort.readline()
    serial_count += 1
    # Resetting the Serial Input Buffer
    if serial_count == 20:
        serialPort.reset_input_buffer()
        serialPort.flush()
        serial_count = 0

def connection_swap():
    global port, connect_status
    port = serial.tools.list_ports.comports()
    coms = [com[0] for com in port]
    if coms:
        connect_status = True
        start_thread()  
        initialise_serial(coms[0])
    else:
        connect_status = False

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
        # Starting serial stuff        
        time.sleep(interval)
        # Only reads serial if read_state is True

        if connect_status == False:
            print("THR [Stopping Thread at port:",port,"]")
            print("Status Thread [stopped]")
            print("PRC [Stopping Serial]")
            print("PRC [Stopping MQTT coms]")
            #client.loop_stop()
            #serialPort.close()
            serial_disconnect()
            break

        if read_state == True:
            serial_read_data()
    
def start_thread():
    print("THR [Starting Thread at port:",port,"]")
    port_controller = threading.Thread(target=check_presence, args=(port, 0.1))
    port_controller.setDaemon(True)
    port_controller.start()

def send_to_controller(value):
    com_string = "".join(str(value[key]) for key in sorted(value))
    data = bytes("FIG" + com_string, 'utf-8')
    serial_send_data(data)

def main():
    connection_swap()
    while True:
        if connect_status:
            print("Polling now")
            response = requests.get("http://127.0.0.1:8000/figurines")
            if response.text == figurine_status:
                print("NO CHANGE")
            else:
                print("IT CHANGED!!!!")
                figurine_status = response.text
                print(figurine_status)
                send_to_controller(figurine_status)
                # Do pyserial stuff
            # Sleep for 15 seconds
            sleep(POLL_DELAY)
        else:
            connection_swap()

if __name__ == "__main__":
    main()
    

