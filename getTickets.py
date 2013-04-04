 #!/usr/bin/python

import serial
import io
import time
import urllib2
import json
import sys
import os

from urllib2 import Request, urlopen, URLError, HTTPError

def getMessages2BPrinted():

	
	#req = urllib2.Request("https://vooruit.yesplan.be/api/events/date%3A20-03-2013%20event%3Aookdagklapper%3A%22Ook%20op%20dagklapper%22?api_key=30BC1A5EF43F9D36A2CA61544CC98A24")
	req = urllib2.Request("http://192.168.2.31/stories/print_to_be_printed_stories/")
	#req = urllib2.Request('http://192.168.2.31')
	
	try:	
		i=0;		
		response = urllib2.urlopen(req)
		data1 = response.read()
		pag=json.loads(data1)
		#print len(pag["data"])
		#for w in pag["data"]:
		#	print pag["data"][i]["name"]
		#	i=i+1
		print len(pag["stories"])
		for w in pag["stories"]:
			print pag["stories"][i]["description"]
			os.system("echo %s > naaikamer.txt" % (pag["stories"][i]["description"]))
			os.system("start /min notepad /P naaikamer.txt")
			time.sleep(1)
			i=i+1
				
	except HTTPError as e:
		print e.code   		
		
		time.sleep(1)
	except URLError as e:
		print 'Reason: ', e.reason
		
	return

#getMessage() # get verhaal

	
