import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 10000)
    sock.bind(server_address)

    while True:
        print('Waiting for a message')
        data, address = sock.recvfrom(4096)

        print(f'Received message: {data} from {address}')

if __name__ == '__main__':
    main()
