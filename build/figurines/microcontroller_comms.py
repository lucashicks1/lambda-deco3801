##########################################################################
#
# @file: microcontroller_comms.py
# @author: Dylan Fleming, 45313345
# @brief: Handler for serial microcontroller communication and
#         communication with database
#
##########################################################################

# =========================== IMPORTS ================================== #

import threading
import time
from time import sleep
from json import JSONDecodeError
import json
import logging

import serial.tools.list_ports
import requests
from serial import SerialException, SerialTimeoutException
# =========================== GLOBAL VALUES ================================== #

POLL_DELAY = 15
COM_PORT_PREFIX = "cu.usbmodem"  # usbmodem1101 and usbmodem2101
MAX_CONNECTION_COUNT = 10

global connect_status, read_state, port, serialPort
global serial_count  # Optimized counter, used to clear the serial input buffer
serial_count = 0
connect_status = False  # Serial connection state
read_state = True  # True when serial starts up connection

# =========================== SERIAL HANDLING ================================== #

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
_LOGGER = logging.getLogger(__name__)

def initialise_serial(port):
    global serialPort, connect_status
    _LOGGER.info("Starting serial at %s", port)
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
    _LOGGER.info("Disconnecting serial port")
    serialPort.flushInput()
    serialPort.flushOutput()
    _LOGGER.info("Flushing input and output")
    serialPort.close()
    _LOGGER.info("Closing serial port")
    connect_status = (
        False  # Set the connection status to False when serial is disconnected
    )


def serial_send_data(data):
    global read_state, serialPort
    read_state = False  # Pause Reading serial
    _LOGGER.info("Sending data to the port")
    _LOGGER.debug("Sending %s", data)
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
    _LOGGER.info("Sending data to the microcontroller")
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
    """Starts a thread that checks serial port presence"""
    global port, connect_status
    _LOGGER.info("Starting thread at port %s", port)
    # target - callable object invoked by the start() or run() command
    # args - arguments passed to check_presence command
    port_controller = threading.Thread(target=check_presence, args=(port, 0.1))
    port_controller.daemon = True
    port_controller.start()


# =========================== MAIN FUNCTIONALITY ================================== #


def main():
    """Main script loop that will attempt to connect to the microcontroller.
    If so, it will send data via serial to move the servo motors
    """

    global port, connect_status
    # figurine_status = {}

    connection_count = 0

    while True:
        if connection_count >= MAX_CONNECTION_COUNT:
            _LOGGER.error("Could not find valid serial connection and timed out, try again")
            return

        if not connect_status:
            port_device = None
            ports = serial.tools.list_ports.comports()
            for port in ports:
                _LOGGER.info("Trying port - %s", port.device)
                if port.name is not None and COM_PORT_PREFIX in port.name:
                    port_device = port[0]
                    break
            connection_count += 1
            if port_device is not None:
                try:
                    initialise_serial(port_device)
                except ValueError as e:
                    _LOGGER.error("Parameter given is out of range")
                    _LOGGER.debug(e)
                except SerialException as e:
                    # SerialException derives from IOError
                    _LOGGER.error("Device can not be found or configured")
                    _LOGGER.debug(e)

                try:
                    start_thread()
                except RuntimeError as e:
                    _LOGGER.error("start() method called more than once for same thread object")
                    _LOGGER.debug(e)

            else:
                connect_status = False
            continue
        if serialPort.is_open:
            try:
                response_body = requests.get('http://127.0.0.1:8000/figurines', timeout=5).text
                if response_body is not None:
                    try:
                        response = json.loads(response_body)
                    except JSONDecodeError as e:
                        _LOGGER.error("Not valid JSON document")
                        _LOGGER.debug(e)
                else:
                    _LOGGER.Error("Got nothing from the api")
                    continue
                try:
                    send_to_controller(response)
                except SerialTimeoutException as e:
                    _LOGGER.error("Write timeout")
                    _LOGGER.debug(e)
                # if response != figurine_status:
                #     figurine_status = response
                #     send_to_controller(figurine_status)
                sleep(POLL_DELAY)
            except requests.exceptions.ConnectionError as e:
                _LOGGER.info("Error making HTTP request")
                _LOGGER.debug("Error - %s", e)
                serial_disconnect()
                _LOGGER.info("Disconnecting serial")
                break
            except serial.SerialException as e:
                _LOGGER.info("Error finding serial device or configuring it")
                _LOGGER.debug("Error - %s", e)
                break




if __name__ == '__main__':
    main()
