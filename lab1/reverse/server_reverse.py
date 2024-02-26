import socket
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''
print("Equation is received")
data = clientConnection.recv(1024)
msg = data.decode()
result = 0
word=msg
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str
k=reverse(word)
result=k
print("Send the result to client")
output = str(result)
clientConnection.send(output.encode())
clientConnection.close()