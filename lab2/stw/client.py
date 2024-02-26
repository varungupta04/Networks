# Client.py

import socket
import time

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    sequence_number = 0
    message = "Hello, Server!"

    while True:
        packet = f"{sequence_number}:{message}"
        client_socket.sendto(packet.encode(), server_address)

        try:
            client_socket.settimeout(5)
            data, addr = client_socket.recvfrom(1024)
            print(f"Received acknowledgment: {data.decode()} from {addr}")

            # Increment sequence number for next packet
            sequence_number += 1
        except socket.timeout:
            print("Timeout! Resending packet...")
            continue

        time.sleep(2)  # Simulating processing time

if __name__ == "__main__":
    client()
