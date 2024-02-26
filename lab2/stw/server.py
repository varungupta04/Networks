# Server.py

import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received: {data.decode()} from {addr}")

        response = "ACK"
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    server()
