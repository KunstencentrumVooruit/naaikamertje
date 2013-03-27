#!/usr/bin/python

import serial
import io
import time
import httplib
import json
import sys

def getMessage(code):

	conn = httplib.HTTPConnection("192.168.2.32")
	conn.request("GET", "/stories/print_story_with_code/%s/" % (code)) 
#	conn = httplib.HTTPSConnection("vooruit.yesplan.be")
#	conn.request("GET", "/api/events?api_key=30BC1A5EF43F9D36A2CA61544CC98A24")
	try:	
		r1 = conn.getresponse()
		print r1.status, r1.reason
		data1 = r1.read()
		pag=json.loads(data1)
		print pag["story"]["description"]
		# print ticket		
		ser.write("0") # print 0 of 2 in geval van afdrukfout 
		time.sleep(1)
	#except ValueError:
	except httplib.BadStatusLine, err:
		if err.code == 404:
       			print "netwut!"
   		else:
       			raise    		
		print "Unexpected error:", sys.exc_info()[0]
		exctype, value = sys.exc_info()[:2]
		if (str(exctype) == "<type 'exceptions.ValueError'>"):
			print "netwerkfout!"		
		ser.write("1") # foute code
		time.sleep(1)
	conn.close()
	return

ser = serial.Serial('/dev/ttyACM0', 9600)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while 1:
	line = ser.readline();
	line = line[:-2]	
	#line.rstrip("\r\n")
	print line
	print map(ord,line) # debugging: print received serial in ASCII
	getMessage(line) # get verhaal
	time.sleep(1)
	#ser.write("11111")




