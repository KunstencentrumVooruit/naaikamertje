#!/usr/bin/python

import serial
import io
import time
import urllib2
import json
import sys
import os
from urllib2 import Request, urlopen, URLError, HTTPError

def getMessage(code):

	req = urllib2.Request("http://192.168.2.31/stories/print_story_with_code/%s/" % (code))
	#req = urllib2.Request('http://192.168.2.31')
	
	try:	
		response = urllib2.urlopen(req)
		data1 = response.read()
		pag=json.loads(data1)
		print pag["story"]["description"]
		# print ticket
		os.system("echo %s > naaikamer.txt" % (pag["story"]["description"]))
		os.system("start /min notepad /P naaikamer.txt")
		ser.write("0") # print 0 of 2 in geval van afdrukfout 
		time.sleep(1)
	except HTTPError as e:
		print e.code   		
		ser.write("1") # foute code
		time.sleep(1)
	except URLError as e:
		print 'Reason: ', e.reason
		ser.write("2") # netwerkfout..
 	return

ser = serial.Serial('COM4', 9600)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while 1:
	line = ser.readline();
	line = line[:-2]	
	print line
	print map(ord,line) # debugging: print received serial in ASCII
	getMessage(line) # get verhaal
	time.sleep(1)
	
