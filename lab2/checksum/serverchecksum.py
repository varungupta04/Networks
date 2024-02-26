import socket
import hashlib

def calculate_checksum(data):
    hash_object = hashlib.sha256()
    hash_object.update(data)
    return hash_object.hexdigest()

def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    connection, address = server_socket.accept()
    print(f"Connection from {address}")

    data = connection.recv(1024)
    print(f"Received data: {data.decode()}")

    checksum_server = calculate_checksum(data)
    print(f"Checksum on server: {checksum_server}")

    connection.send(checksum_server.encode())

    connection.close()
    server_socket.close()

if __name__ == "__main__":
    server()
