import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
word=input("Enter the string ")
inp = word
client.send(inp.encode())
answer = client.recv(1024)
print("Reverse String is "+answer.decode())
client.close