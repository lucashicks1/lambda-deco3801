import socket


def connect_to_esp32(esp32_ip, esp32_port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the ESP32
        client_socket.connect((esp32_ip, esp32_port))
        print(f'Connected to {esp32_ip}:{esp32_port}')

        while True:
            message = input("Enter a message to send (or 'exit' to quit): ")

            # Send the message to the ESP32
            client_socket.sendall(message.encode())

            if message.lower() == 'exit':
                break

        # Close the socket
        client_socket.close()
    except Exception as e:
        print(f'Connection failed: {e}')


# Example usage
if __name__ == '__main__':
    esp32_ip = 'ESP32_IP_ADDRESS'
    esp32_port = 12345  # Change this to the port your ESP32 is listening on

    connect_to_esp32(esp32_ip, esp32_port)
