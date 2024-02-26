# Server.py

import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    expected_sequence_number = 0

    while True:
        data, addr = server_socket.recvfrom(1024)
        sequence_number, message = data.decode().split(":")
        sequence_number = int(sequence_number)

        if sequence_number == expected_sequence_number:
            print(f"Received: {message} from {addr}")

            response = f"ACK:{sequence_number}"
            server_socket.sendto(response.encode(), addr)

            expected_sequence_number += 1
        else:
            print(f"Discarded out-of-order packet with sequence number {sequence_number}")

if __name__ == "__main__":
    server()
