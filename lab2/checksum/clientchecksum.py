import socket
import hashlib

def calculate_checksum(data):
    hash_object = hashlib.sha256()
    hash_object.update(data)
    return hash_object.hexdigest()

def client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, Server!"
    print(f"Sending data: {message}")

    checksum_client = calculate_checksum(message.encode())
    print(f"Checksum on client: {checksum_client}")

    client_socket.send(message.encode())

    received_checksum = client_socket.recv(1024).decode()
    print(f"Received checksum from server: {received_checksum}")

    if checksum_client == received_checksum:
        print("Data integrity verified: Checksums match!")
    else:
        print("Data integrity NOT verified: Checksums do not match!")

    client_socket.close()

if __name__ == "__main__":
    client()
