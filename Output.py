import IdList
import re
from MainProgram import identifierTable
class Output:		
	def __init__(self, t):
		self.iList = IdList.IdList(t)
		self.t = t
 
	def parse(self):
		x = int(self.t.getToken())
		if x != 11:
			print "write keyword expected."
			exit()
 
		self.iList.parse()
 		x = int(self.t.getToken())
		if x != 12:
			print "Missing semicolon."
			exit()
	
	def execute(self):
		# List of identifiers
		l = re.split(',', self.iList.execute())
		# Print the corresponding identifiers
		for key in l:
			x = -1
			for y in xrange(0, len(identifierTable)):
				if identifierTable[y][0] == key:
					x = y
			if x >= 0 and identifierTable[x][1] != None:
				print identifierTable[x][0] + ' = ' + str(identifierTable[x][1])
			elif x >= 0 and identifierTable[x][1] == None:
				print 'Variable was never initialized.'
				exit()
			else:
				print '%s not in variable table.' % i
				exit()
 
	def Print(self):
		return 'write ' + self.iList.Print() + ';' 
