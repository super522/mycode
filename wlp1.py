import socket
import sys

host="localhost"
port=8000


sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_addr = (host, port)

print("Connecting to %s:%d" %(host, port))
sk.connect(server_addr)


while True:
	message = input("Type something to send. or type'q' to quit:")
	sk.sendall(message.encode('utf-8'))
	if message == "q":
		break;

	data = sk.recv(80)
	print(data.decode('utf-8'))

print("Closing socket ...")
sk.close()

