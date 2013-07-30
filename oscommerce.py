#!/usr/bin/env python

"""carane nganggo kepriwer
aku yo sitik le ngerti
wkwkwk"""

print '###### osCommerce password generator ######'
print '###### JS by Michael Calabrese       ######'
print '###### Python by Ken Eddy            ######'

import random,hashlib

plain = raw_input("Please insert your plain-text : ")
bulat = round(random.random()*25)
clan  = bulat+97
def createRandomLowerCaseLetter():
	resultRandom = chr(clan)
	return resultRandom


def cryptokey(plain):
	salt = ''
	for x in range(0,100):
		salt += createRandomLowerCaseLetter()
	salter = hashlib.md5(salt+plain).hexdigest()
	substr = salter[0:2]
	passwd = hashlib.md5(substr+plain).hexdigest() + ':' + substr
	return passwd

print cryptokey(plain)
