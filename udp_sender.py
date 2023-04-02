import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 10000)
    message = b'This is a test message.'

    try:
        # Send the message to the server
        print(f'Sending message: {message}')
        sent = sock.sendto(message, server_address)

    finally:
        print('Closing socket')
        sock.close()

if __name__ == '__main__':
    main()
