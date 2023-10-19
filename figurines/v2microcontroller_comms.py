from threading import Thread
from time import sleep
from json import JSONDecodeError
import json
import logging

import serial.tools.list_ports
import requests
from serial import SerialException, SerialTimeoutException, Serial



CONNECTION_DELAY = 5
COM_PORT_PREFIX = "cu.usbmodem"  # usbmodem1101 and usbmodem2101
MAX_CONNECTION_COUNT = 25
READ_INTERVAL = 0.1

API_ENDPOINT = "http://127.0.0.1:8000/figurines"
API_REQUEST_TIMEOUT = 5
POLL_DELAY = 15

read_state = True
serial_count = 0
serial_port: Serial | None = None

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
_LOGGER = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(logging.DEBUG)

def check_presence(port: str, interval: int = READ_INTERVAL):
    while True:
        sleep(interval)
        if serial_port is None:
            _LOGGER.error("THR [Stopping Thread at port: %s]", port)
            _LOGGER.error("Status Thread [stopped]")
            _LOGGER.error("PRC [Stopping serial]")
            serial_disconnect(serial_port)
        
        if read_state:
            serial_read_data(serial_port)


def initialise_serial() -> Serial | None:
    port = None
    available_ports = serial.tools.list_ports.comports()
    for port_option in available_ports:
        if port_option.name is not None and COM_PORT_PREFIX in port_option.name:
            port = port_option[0]
            break
    if port is None:
        return None
    try:
        serial_port = Serial(
            port, baudrate=9600, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE
        )
        return serial_port
    except ValueError as e:
        _LOGGER.error("Parameter given is out of range")
        _LOGGER.debug(e)
        return None

    except SerialException as e:
        # SerialException derives from IOError
        _LOGGER.error("Device can not be found or configured")
        _LOGGER.debug(e)
        return None

def ping_api() -> dict | None:
    response_body = requests.get(API_ENDPOINT, timeout=API_REQUEST_TIMEOUT).text
    if response_body is None:
        _LOGGER.info("Received nothing from the api endpoint.")
        return None
    try:
        response = json.loads(response_body)
        return response
    except JSONDecodeError as e:
        _LOGGER.error("Not valid JSON document")
        _LOGGER.debug(e)
        return None

def serial_disconnect(serial_port: Serial):
    _LOGGER.info("Disconnecting the serial port.")
    serial_port.reset_input_buffer()
    serial_port.reset_output_buffer()
    _LOGGER.info("Reset both input and output buffers.")
    serial_port.close()
    _LOGGER.info("Closed serial port.")

def serial_send_data(data: dict):
    global serial_port
    byte_stream: bytes = convert_response(data)

    _LOGGER.info("Sending data to the port")
    _LOGGER.debug("Sending %s to the port", str(byte_stream))

    try:
        serial_port.write(byte_stream)
        return serial_port
    except SerialTimeoutException as e:
        _LOGGER.error("Write timeout")
        _LOGGER.debug(e)
    except SerialException as e:
        _LOGGER.error("Encountered serial exception")
        _LOGGER.debug(e)
        serial_port = None

def serial_read_data(serial_port: Serial):
    serial_string: str = str(serial_port.readline())
    if serial_string is not None:
        _LOGGER.info("Received data from MC: %s", serial_string)

    serial_count += 1
    if serial_count == 20:
        serial_port.reset_input_buffer()
        serial_port.flush()
        serial_disconnect(serial_port)


def convert_response(response: dict) -> bytes:
    _LOGGER.info("Converting response data to bytes")
    com_string = ''.join(str(response[key]) for key in sorted(response))
    data = 'FIG' + com_string
    return bytes(data, encoding='utf-8')

def start_thread(port: str):
    _LOGGER.info("Starting thread at port %s", port)
    # target - callable object invoked by the start() or run() command
    # args - arguments passed to check_presence command
    port_controller: Thread = Thread(target=check_presence, args=(port, READ_INTERVAL))
    port_controller.daemon = True
    try:
        port_controller.start()
    except RuntimeError as e:
        _LOGGER.error("Start() method called multiple times on the same thread object")
        _LOGGER.debug(e)

def main():
    global serial_port
    connection_count: int = 0
    figurine_status: dict = {}
    while True:
        _LOGGER.info("Trying to connect to serial")
        for _ in range(MAX_CONNECTION_COUNT):
            serial_port = initialise_serial()
            if serial_port is not None:
                break
            connection_count += 1
            sleep(CONNECTION_DELAY)

        if serial_port is None:
            _LOGGER.error("Could not find valid serial connection and timed out, try again")
            continue

    
        while serial_port is not None:
            try:
                serial_port.read()
            except SerialException as e:
                serial_port = None
                figurine_status = {}
                continue
            try:
                _LOGGER.info("Making request to API")
                response = ping_api()
                sleep(POLL_DELAY)
            except requests.exceptions.ConnectionError as e:
                _LOGGER.info("Error making HTTP request")
                _LOGGER.debug("Error - %s", e)
                sleep(POLL_DELAY * 2)
                continue

            if response is None:
                continue

            if response != figurine_status:
                figurine_status = response
                serial_send_data(response)





if __name__ == "__main__":
    main()
