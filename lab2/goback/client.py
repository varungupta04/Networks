# Client.py

import socket
import time

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    base = 0
    window_size = 3
    sequence_number = 0

    messages = ["Hello", "Go", "Back", "N"]

    while base < len(messages):
        for i in range(base, min(base + window_size, len(messages))):
            packet = f"{sequence_number}:{messages[i]}"
            client_socket.sendto(packet.encode(), server_address)
            print(f"Sent: {messages[i]} with sequence number {sequence_number}")
            sequence_number += 1

        try:
            client_socket.settimeout(5)
            while True:
                data, addr = client_socket.recvfrom(1024)
                ack_sequence_number = int(data.decode().split(":")[1])
                print(f"Received acknowledgment for sequence number {ack_sequence_number}")

                if ack_sequence_number == base:
                    base += 1
                    break
        except socket.timeout:
            print("Timeout! Resending window...")

    print("All messages sent successfully.")

if __name__ == "__main__":
    client()
