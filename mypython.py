#! /usr/bin/python

# Eric Gullufsen - Operating Systems I - Python Exploration (Program 5)
# August 4, 2015

import os
import string
from random import SystemRandom as sysrand

# Instantiate our random number generator object, which this implementation uses system 
# calls and is more secure (according to the pydocs) than the usual functions in the random module
generator = sysrand()

names = ["eric1.txt", "eric2.txt", "eric3.txt"]

# loop over the names array
for name in names:
	writey = ""
	# open a file for writing and reading, creating it if it doesn't yet exist
	with open(name, "w+") as filey:
		for x in range(10): # Ten random characters is what we need
			index = generator.randint(0,25) # get a pseudo-random index of the alphabet
			charizard = string.lowercase[index] # get character at that index
			writey += charizard 
		filey.write(writey)
		filey.seek(0) # jump back up to beginning of file before reading its contents into memory
		output = filey.read()
		print 'contents of {0} are: {1}\n'.format(name, output)
	
num_1 = generator.randint(1,42)
num_2 = generator.randint(1,42)

print 'random number number one is: {0}\nrandom number number two is {1}\nTheir product being: {2}'.format(num_1,num_2,(num_1 * num_2)) 
