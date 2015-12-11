#!/usr/bin/env python

import socket

def convert_integer():
	data = 1234
	#32-bit
	print "Original : %s => long host byte order %s, network byte order: %s" % \
		(data, socket.ntohl(data), socket.htonl(data))
	#16-bit
	print "Original : %s => short host byte order %s, network byte order: %s" % \
		(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
	convert_integer()