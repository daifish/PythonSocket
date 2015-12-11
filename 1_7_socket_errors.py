#!/usr/bin/env python

import sys
import socket
import argparse

def main():
	#setup argument parsing
	parser = argparse.ArgumentParser(description='Socket Error Example')
	parser.add_argument('--host', action="store", dest="host", required=False)
	parser.add_argument('--port', action="store", dest="port", type=int, required=False)
	parser.add_argument('--file', action="store", dest="file", required=False)
	#get the argument
	#for example: python xxx.py --host=www.baidu.com --port=8080 --file=xxx.py
	given_args = parser.parse_args()
	host = given_args.host
	port = given_args.port
	print port
	filename = given_args.file

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" % e
		sys.exit(1)

	try:
		#connect((host, port))
		s.connect((host, port))
	except socket.gaierror, e:
		print "Address-related error connecting to server: %s" % e
		sys.exit(1)
	except socket.error, e:
		print "Connect error : %s" % e
		sys.exit(1)

	try:
		s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
	except socket.error, e:
		print "Error sending data: %s" % e
		sys.exit(1)

	while 1:
		try:
			buf = s.recv(2048)
		except socket.error, e:
			print "Error receive data : %s" %e
			sys.exit(1)
		if not len(buf):
			break
		sys.stdout.write(buf)

if __name__ == '__main__':
	main()


