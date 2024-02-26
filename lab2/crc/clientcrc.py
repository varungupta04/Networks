import socket
import binascii

def calculate_crc(data):
    return binascii.crc32(data) & 0xFFFFFFFF

def client(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 8080))
        crc = calculate_crc(message.encode())
        crc_bytes = crc.to_bytes(4, byteorder='big')
        message_with_crc = message.encode() + crc_bytes
        client_socket.sendall(message_with_crc)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    message = "Hello, server! This is a test message."
    client(message)
