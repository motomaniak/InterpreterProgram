import IdList
from MainProgram import identifierTable
import re

class Input:
	def __init__(self, t, inData):
		self.iList = IdList.IdList(t)
		self.t = t
		self.inData = inData
 
	def parse(self):
		x = int(self.t.getToken())
		if x != 10:
			print 'read keyword expected.'
			exit()
 
		self.iList.parse()
 		x = int(self.t.getToken())
		if x != 12:
			print 'Missing semicolon.'
			exit()
 
	def execute(self):	
		# Split the returned list from IdList by the comma delimiter and store in list
		l = re.split(',', self.iList.execute())
		# For every variable in the list, assign it a value if it's in the table and then remove from inData
		for key in l:
			x = -1
			for y in xrange(0, len(identifierTable)):
				if identifierTable[y][0] == key:
					x = y
			if x >= 0 and len(self.inData) > 0:
				self.iList.setId(int(self.inData[0]))
				del self.inData[0]
			elif len(inData) == 0:
				print 'Insufficient amount of read data'
				exit()
			else:
				print '%s variable not declared.' % i
				exit()
 
	def Print(self):
		return 'read ' + self.iList.Print() + ';'
