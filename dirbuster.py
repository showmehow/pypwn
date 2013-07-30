#!/usr/bin/env python

import urllib2
import sys
import os

print """
Directory Scanner v.0.1
Ken Eddy - files.eddy@gmail.com
"""

#if len(sys.argv) != 2:
#	sys.stderr.write('Usage: '+sys.argv[0]+' URL DIRLIST\n\n')
#	sys.exit(1)

#if os.path.exists(sys.argv[2]):
#	sys.stderr.write('Wrong path of DIRLIST')
#	sys.exit(1)

url = sys.argv[1]
open_dir_list = open("dirlist.txt",'r')
dirs = open_dir_list.read().split("\n")
open_dir_list.close()

for dir in dirs:
	
	uri = url+dir

	try:
		response = urllib2.urlopen(uri)
		if response:
			print response.info()
			if response.getcode() == 200:
				print "[+] FOUND %s " % (uri)
			
	except urllib2.HTTPError, e:
		if e.code == 401:
			print "[!] Authorization Required %s " % (uri)
		elif e.code == 403:
			print "[!] Forbidden %s " % (uri)
		elif e.code == 404:
			print "[-] Not Found %s " % (uri)
		elif e.code == 503:
			print "[!] Service Unavailable %s " % (uri)
		else:
			print "[?] Unknwon"
		
	

print "\n:. FINISH :.\n"
	