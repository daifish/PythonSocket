#!/usr/bin/env python

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print 'Connect to %s port %s' %server_address
	sock.connect(server_address)

	try:
		message = "Test message. This will be echoed"
		print "send %s" %message
		sock.sendall(message)
		amount_received = 0
		amount_excepted = len(message)
		while amount_received < amount_excepted:
			data = sock.recv(16)
			amount_received += len(data)
			print "Receive %s" % data
	except:
		print "socket exception"
	finally:
		print "close the conncetion"
		sock.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Server Example')
	parser.add_argument('--port', action='store', type=int, dest='port', required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)