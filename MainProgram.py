import sys
import Tokenizer
import program
import re

identifierTable = []
if __name__ == "__main__":
	# Open file with command line argument. Check for existence, then tokenize the file	
	with open(sys.argv[1], 'r') as f:
		t = Tokenizer.Tokenizer(f)
	
	inData = []
	if(len(sys.argv) > 2):

		# Grab the data from the inputFile and split it by spaces
		with open(sys.argv[2], 'r') as file:
			inData = re.split(r'[ \t]+', file.readline())
 	
		# Remove any leftover white spaces
		inData = [s.strip() for s in inData]
		for i in inData:
			if not int(i):
				print 'Your input data must be of type integer.'
				exit()

	# Initialize, parse, print, and then execute the input program
	program = program.Program(t, inData)
	program.parse()
	program.Print()
	program.execute()
 
	# Garbage collection
	t.__del__
	program.__del__
