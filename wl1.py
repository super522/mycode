import socket
import sys

s="f.txt"

host="localhost"
port=8000

server_addr = (host,port)

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("binding to %s:%d"%(host,port))
sk.bind(server_addr)

print("Listening on %s:%d"%(host,port))
sk.listen(5)

print("wanting for client to connect...")
cli_sk,cli_addr = sk.accept()

print("client %s:%d is coming"%(cli_addr[0],cli_addr[1]))

while True:
	data = cli_sk.recv(80)
	if data == "q":
		break;
	if data == "x":
		z=open(s,"r")
		p=z.read()
		print(p)

	print("CLIENT:"+ data.decode('utf-8'))
	msg = "SERVER ECHO:"+ data.decode('utf-8')
	cli_sk.sendall(msg.encode('utf-8'))

print("Closing socket ...")
sk.close()