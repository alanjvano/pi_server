import socket
import sys
import argparse

# argument parser
parser = argparse.ArgumentParser(description="client")
parser.add_argument('-a', '--address', required=True, help='TCP socket address')
parser.add_argument('-p', '--port', required=True, help='TCP port')
args = vars(parser.parse_args())
#print(args)

# Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args['address'], int(args['port']))
print('connecting to {} | {}'.format(server_address[0], server_address[1]))
sock.connect(server_address)

try:
	message = 'this is a message...'
	print('sending: \'{}\''.format(message))
	sock.sendall(bytes(message, "utf-8"))
	msg_rcv = ''

	while True:
		data = sock.recv(8)
		print('received: {}'.format(data))
		msg_rcv += data.decode("utf-8")
		if msg_rcv == message:
			break
finally:
	print('final message: {}'.format(msg_rcv))
	sock.close()
