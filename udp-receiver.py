import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('192.168.1.100', 10000)
    sock.bind(server_address)

    while True:
        print('Waiting for a message')
        data, address = sock.recvfrom(4096)

        print(f'Received message: {data} from {address}')

        # Echo the message back to the sender
        sent = sock.sendto(data, address)

if __name__ == '__main__':
    main()
