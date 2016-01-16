#!/usr/bin/python

#THIS PYTHON SCRIPT PERFORMS A CAESAR SHIFT TO ENCODE OR DECODE AN INPUT TEXTFILE
#AUTHOR: CRISTOBAL MITCHELL
#DATE MODIFIED: 11/1/2015
#VERSION 0.0.1


#TODO

#DEBUG FLAG

debug = False


import sys
import os
import argparse

if debug:
	print "All modules have been imported"


class CAESAR:

	#CLASS ATTRIBUTES


	#MEMBER FUNCTIONS BELOW

	def __init__(self):

		print("")
		print("Starting CAESAR CIPHER...")
		print("")
		
		
	#THIS FUNCTION ENCODES OPENED FILE
	def encodeFile(self):
		f = open(raw_input("What file do you want to encode?"),"rU")
		shift = int(raw_input("How many charaters do you want to shift?"))
		encodedText=""
		#for i in range(0,len(alphabet)):
			#dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]
		
		for each in f.readlines():
			c = (ord(each)+shift) % 126
			if c < 32:
				c+=31
			encodedText+=chr(c)
			return writeEncodedFile(encodedText)
			f.close()
        	
		if debug: 
			print "The encoded text is" 
			print encodedText

	#THIS FUNCTION DECODES OPENED FILE
	def decodeFile(self,f,shift):
		alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		dic={}
		decodedText=""
		for i in range(0,len(alphabet)):
			dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]
		
		for l in f.lower():
			if l in dic:
				l=dic[l]
				decodedText+=l
		return writeEncodedFile(decodedText)
        	
		
	#THIS FUNCTION WRITES ENCODED FILE TO DESKTOP
	def writeEncodedFile(self,encodedText):
		self.encryptedLocation = os.path.join(os.path.expanduser('~'), 'Desktop')
		self.encryptedFilePath = os.path.join(self.encryptedLocation,"Ecrypted.txt")
		self.encryptedFile = open (self.encryptedFilePath, "w")
		self.encryptedFile.write(encodedText)
		self.encryptedFile.close()
		if debug: 
			print ""


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="""Encrypt or Decrypt text file. Encoded or decoded text are saved to the desktop. """)
	
	parser.add_argument('--encode','-e', action="store_true", help='Encodes plain text file.')
	parser.add_argument('--decode','-d', action="store_true", help='Decodes plain text file.')
	
	args = parser.parse_args()

	if args.encode or args.decode:
		
		c = CAESAR()
		if args.encode:
			c.encodeFile()

		elif args.decode:
			c.decodeFile()
	else:
		print "You must do either --encode or -e or --decode or -d. See -h for help."


	





