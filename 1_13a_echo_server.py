#!/usr/bin/env python

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
	#create the socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#enable reuse the address/port
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#bind the socket to the port
	server_address = (host, port)
	print "Start up echo server on %s port %s" %server_address
	sock.bind(server_address)
	#listen the clients
	sock.listen(backlog)
	while True:
		print "wait to receive message from client"
		client, address = sock.accept()
		data = client.recv(data_payload)
		if data:
			print "Data: %s" %data
			client.send(data)
			print "send %s bytes back to %s" % (data, address)
			client.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Server Example')
	parser.add_argument('--port', action='store', dest='port', type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server(port)
