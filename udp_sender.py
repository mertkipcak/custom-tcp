import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('192.168.1.100', 10000)
    message = b'This is a test message.'

    try:
        # Send the message to the server
        print(f'Sending message: {message}')
        sent = sock.sendto(message, server_address)

        # Receive the echoed message
        print('Waiting for the echoed message')
        data, address = sock.recvfrom(4096)
        print(f'Received echoed message: {data} from {address}')

    finally:
        print('Closing socket')
        sock.close()

if __name__ == '__main__':
    main()
