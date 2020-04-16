import socket
import sys

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',10000)
print('starting socket on {} on port {}'.format(server_address))
sock.listen(1)

while True:
	print('ready for connection')
	connect, client_address = sock.accept()
	try:
		print('new connection: {})
