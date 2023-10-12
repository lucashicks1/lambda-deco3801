##########################################################################
#
# @file: microcontroller_comms.py
# @author: Dylan Fleming, 45313345
# @brief: Handler for serial microcontroller communication and
#         communication with database
#
##########################################################################

# =========================== IMPORTS ================================== #

import serial.tools.list_ports
import threading
import time
from time import sleep
import requests
import socket
import json

# =========================== GLOBAL VALUES ================================== #

POLL_DELAY = 15
global connect_status, read_state, port, serialPort
global serial_count  # Optimized counter, used to clear the serial input buffer
serial_count = 0
connect_status = False  # Serial connection state
read_state = True  # True when serial starts up connection

# =========================== SERIAL HANDLING ================================== #


def initialise_serial(port):
    global serialPort, connect_status
    print('PRC [Starting Serial at ' + port + ']')
    serialPort = serial.Serial(
        port,
        baudrate=9600,
        bytesize=8,
        timeout=0,
        stopbits=serial.STOPBITS_ONE,
    )
    connect_status = (
        True  # Set the connection status to True when serial is initialized
    )


def serial_disconnect():
    global serialPort, connect_status
    serialPort.flushInput()
    serialPort.flushOutput()
    serialPort.close()
    connect_status = (
        False  # Set the connection status to False when serial is disconnected
    )


def serial_send_data(data):
    global read_state, serialPort
    read_state = False  # Pause Reading serial
    print('Sending ' + str(data))
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


def send_to_controller(value):
    com_string = ''.join(str(value[key]) for key in sorted(value))
    data = bytes('FIG' + com_string, 'utf-8')
    serial_send_data(data)


# =========================== THREADING ================================== #


def check_presence(port, interval=0.01):
    while True:
        time.sleep(interval)
        if not connect_status:
            print('THR [Stopping Thread at port:', port, ']')
            print('Status Thread [stopped]')
            print('PRC [Stopping Serial]')
            serial_disconnect()
            break

        if read_state:
            serial_read_data(serialPort)  # Pass serialPort as a parameter


def start_thread():
    global port, connect_status
    print('THR [Starting Thread at port:', port, ']')
    port_controller = threading.Thread(target=check_presence, args=(port, 0.1))
    port_controller.daemon = True
    port_controller.start()


# =========================== MAIN FUNCTIONALITY ================================== #


def main():
    global port, connect_status
    figurine_status = {}

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
                response = json.loads(
                    requests.get('http://127.0.0.1:8000/figurines').text
                )
                if response != figurine_status:
                    figurine_status = response
                    send_to_controller(figurine_status)
                sleep(POLL_DELAY)
            except Exception as e:
                serial_disconnect()
                print(f'Error connecting to serial: {e}')


if __name__ == '__main__':
    main()
