import sys
import pdb

try:
  # open file stream
	file_name = sys.argv[1];
	corefile = open(file_name, "r")
except IOError:
	print "There was an error reading from ", file_name
  	sys.exit()

def token_number(argument):
	if(argument.isdigit()): return "31"
	switcher = {
		"program": 1,
		"begin": 2,
		"end": 3,
		"int": 4, 
		"if": 5, 
		"then": 6, 
		"else": 7, 
		"while": 8, 
		"loop": 9, 
		"read": 10, 
		"write": 11,
		";": 12, 
		",": 13,
		"=": 14,
		"!": 15,
		"[": 16,
		"]": 17,
		"&&": 18,
		"||" : 19,
		"(": 20, 
		")": 21,
		"+": 22,
		"-": 23,
		"*": 24,
		"!=": 25,
		"==": 26,
		"<": 27,
		">": 28,
		"<=": 29,
		">=": 30,
	}
	return switcher.get(argument, "nothing")

strings = corefile.read()
#new_strings = strings.split()
#print strings
#for string in new_strings:
	#print "#"+ string + "#"
	#print token_number(string)
def get_token(strings):
	for i in range (cursor, len(strings))
 
