import socket
import sys

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',40000)
print('starting socket on {} on port {}'.format(server_address[0], server_address[1]))
sock.bind(server_address)
sock.listen(1)

while True:
	print('ready for connection')
	connection, client_address = sock.accept()
	try:
		print('new connection:{}'.format(client_address))
		while True:
			data = connection.recv(16)
			print('received: {}'.format(data))
			if data:
				connection.sendall(data)
			else:
				break
	except KeyboardInterrupt:
		print('detected interrupt')
		connection.close()
		sys.exit()
	finally:
		connection.close()
