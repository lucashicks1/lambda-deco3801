from threading import Thread
from time import sleep
from json import JSONDecodeError
import json
import logging

import serial.tools.list_ports
import requests
from serial import SerialException, SerialTimeoutException, Serial

CONNECTION_DELAY = 5  # Delay in seconds before attempting to reconnect serial
COM_PORT_PREFIX = "cu.usbmodem"  # usbmodem1101 and usbmodem2101 - serial port open for mac
MAX_CONNECTION_COUNT = 25  # Maximum number of connection attempts to serial before closing progarm
READ_INTERVAL = 0.1  # Time interval in seconds before reading serial data if sent

API_ENDPOINT = "http://127.0.0.1:8000/figurines"  # API Endpoint used to get calendar data
API_REQUEST_TIMEOUT = 5  # Tiemout value in seconds before request times out
POLL_DELAY = 15  # Delay in seconds inbetween polling for figurines

read_state = True  # Global used to determine read/write state of serial port
serial_count = 0  # Count of serial reads before switching over to write
serial_port: Serial | None = None  # Pyserial serial port class instance

# Configures logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
_LOGGER = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(logging.DEBUG)

def check_presence(port: str, interval: int = READ_INTERVAL):
    """Checks the presence of a port, checking if it is still open. This is run on a seperate thread.
    Will also read data from serial port if read_state is set to true

    Args:
        port (str): name of serial port used
        interval (int, optional): Interval of time between function runs. Defaults to READ_INTERVAL.
    """
    while True:
        sleep(interval)
        if serial_port is None:
            # If port is closed, log the errors and flush input/output in disconnect
            _LOGGER.error("THR [Stopping Thread at port: %s]", port)
            _LOGGER.error("Status Thread [stopped]")
            _LOGGER.error("PRC [Stopping serial]")
            serial_disconnect(serial_port)
        
        # Reads data from serial port
        if read_state:
            serial_read_data(serial_port)


def initialise_serial() -> Serial | None:
    """Attempts to connect to a valid serial port.

    Returns:
        Serial | None: returns an Serial instance used in pyserial methods
    """
    port = None
    available_ports = serial.tools.list_ports.comports()
    # Goes through every available port and checks if if is a usb device
    for port_option in available_ports:
        if port_option.name is not None and COM_PORT_PREFIX in port_option.name:
            port = port_option[0]
            break
    # If no port is found, return from function
    if port is None:
        return None
    # Try to connect with the given port and handle any exceptions
    try:
        serial_port = Serial(
            port, baudrate=9600, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE
        )
        return serial_port
    # Parameters given to Serial() are incorrect
    except ValueError as e:
        _LOGGER.error("Parameter given is out of range")
        _LOGGER.debug(e)
        return None

    # Serial device can't be found or is misconfigured
    except SerialException as e:
        # SerialException derives from IOError
        _LOGGER.error("Device can not be found or configured")
        _LOGGER.debug(e)
        return None

def ping_api() -> dict | None:
    """Sends a GET request to the database API and gets data

    Returns:
        dict | None: figurines data
    """
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
    """Disconnects the current serial port, flushing the input and output buffers

    Args:
        serial_port (Serial): serial port instance to disconect
    """
    _LOGGER.info("Disconnecting the serial port.")
    serial_port.reset_input_buffer()
    serial_port.reset_output_buffer()
    _LOGGER.info("Reset both input and output buffers.")
    serial_port.close()
    _LOGGER.info("Closed serial port.")

def serial_send_data(data: dict):
    """Sends figurine data to the serial port

    Args:
        data (dict): serial data to convert to bytes and send
    """
    global serial_port
    byte_stream: bytes = convert_response(data)

    _LOGGER.info("Sending data to the port")
    _LOGGER.debug("Sending %s to the port", str(byte_stream))

    try:
        serial_port.write(byte_stream)
        return serial_port
    except SerialTimeoutException as e:
        _LOGGER.error("Write timeout to serial port")
        _LOGGER.debug(e)
    except SerialException as e:
        _LOGGER.error("Encountered serial exception")
        _LOGGER.debug(e)
        serial_port = None

def serial_read_data(serial_port: Serial):
    """Reads any data from the serial port and logs it

    Args:
        serial_port (Serial): serial port to read data from
    """
    serial_string: str = str(serial_port.readline())
    if serial_string is not None:
        _LOGGER.info("Received data from MC: %s", serial_string)

    serial_count += 1

    if serial_count == 20:
        serial_port.reset_input_buffer()
        serial_port.flush()
        serial_disconnect(serial_port)


def convert_response(response: dict) -> bytes:
    """Converts the response from API and turns it into bytes to send to the serial port

    Args:
        response (dict): response from the API

    Returns:
        bytes: bytes to send to the serial port
    """
    _LOGGER.info("Converting response data to bytes")
    com_string = ''.join(str(response[key]) for key in sorted(response))
    data = 'FIG' + com_string
    return bytes(data, encoding='utf-8')

def start_thread(port: str):
    """Starts a thread to then check the ports

    Args:
        port (str): port name which is being read from - used for logging
    """
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
    """Main program loop which will constantly attempt to connect to a serial device and when connected will write/read to serial.
    """
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
                _LOGGER.error("Serial port not configured/connected.")
                _LOGGER.debug(e)
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
