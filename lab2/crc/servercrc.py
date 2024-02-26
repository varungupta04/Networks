import socket
import binascii

def calculate_crc(data):
    return binascii.crc32(data) & 0xFFFFFFFF

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1)
    print("Server listening on port 8080...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = b""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            data += chunk

        if not data:
            break

        received_crc, message = data[-4:], data[:-4]
        received_crc = int.from_bytes(received_crc, byteorder='big')

        print("Received Message (Hex):", binascii.hexlify(message).decode())
        print("Received CRC (Hex):", hex(received_crc))
        print("Calculated CRC (Hex):", hex(calculate_crc(message)))

        if calculate_crc(message) == received_crc:
            print("Message received without errors:", message.decode())
        else:
            print("Error in received message.")

        conn.close()

if __name__ == "__main__":
    server()
