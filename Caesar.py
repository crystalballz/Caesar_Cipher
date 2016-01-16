#!/usr/bin/python

#THIS PYTHON SCRIPT PERFORMS A CAESAR SHIFT TO ENCODE AN INPUT TEXTFILE
#AUTHOR: CRISTOBAL MITCHELL
#DATE MODIFIED: 1/16/2016
#VERSION 0.0.2


#TODO

#DEBUG FLAG

debug = False


import sys
import os

if debug:
	print "All modules have been imported"


class CAESAR:

	def __init__(self):

		print("")
		print("Starting CAESAR CIPHER...")
		print("")

		self.encryptedFilePath = ""
	
	#THIS FUNCTION DETERMINES WHAT FILE TO OPEN AND ENCODE
	def openFile(self):
		mode = raw_input('Encode or Decode?')
		
		if mode == 'encode':
			fileOpen = open(raw_input('What input file do you want to use?'),'rU')
			message = fileOpen.read()
			shift = int(raw_input('How many charaters do you want to shift?'))
			self.encodeFile(message,shift)
		elif mode == 'decode':
			fileOpen = open(raw_input('What input file do you want to use?'),'rU')
			message = fileOpen.read()
			shift = int(raw_input('What is the key?'))
			self.decodeFile(message,shift)
		elif mode == 'brute':
			fileOpen = open(raw_input('What input file do you want to use?'),'rU')
			message = fileOpen.read()
			self.bruteFile(message,mode)
		elif mode == 'exit':
			exit
		else:
			print "You did not make a valid selection."
			self.openFile()
	
	#THIS FUNCTION ENCODES OPENED FILE
	def encodeFile(self,message,shift):		
		encodedText=""
		for l in message:
			c = (ord(l)+shift) % 126
			if c < 32:
				c+=31
			encodedText+=chr(c)
		self.writeFile(encodedText,"encode")
     

	def bruteFile(self,message,brute):
		bruteText=""
		for i in range(1,95,1):
			for l in message:
				c = (ord(l)-i) % 126
				if c < 32:
					c+=95
				bruteText+=chr(c)
			bruteText+="\n"
		self.writeFile(bruteText,"brute")


	def decodeFile(self,message,shift):		
		decodedText=""
		for l in message:
			c = (ord(l)-shift) % 126
			if c < 32:
				c+=95
			decodedText+=chr(c)
		self.writeFile(decodedText,"decode")
        	
	#THIS FUNCTION WRITES ENCODED FILE TO DESKTOP
	def writeFile(self,text,mode):
		self.encryptedLocation = os.path.join(os.path.expanduser('~'), 'Desktop')
		self.encryptedFilePath = os.path.join(self.encryptedLocation, mode + ".txt")
		self.encryptedFile = open(self.encryptedFilePath, "w")
		self.encryptedFile.write(text)
		self.encryptedFile.close()
		if debug: 
			print ""


if __name__ == "__main__":
	c = CAESAR()
	c.openFile()


	





