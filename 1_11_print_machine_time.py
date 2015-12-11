#!/usr/bin/env python

import ntplib
from time import ctime

def print_time():
	ntp_clinet = ntplib.NTPClient()
	response = ntp_clinet.request('pool.ntp.org')
	print ctime(response.tx_time)

if __name__ == '__main__':
	print_time()