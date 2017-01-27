import pdb
from MainProgram import identifierTable
class Id:			
	def __init__(self,t):
		self.name = ""
		self.t = t
 
	def parse(self):
		self.name = self.t.getValue()
		self.t.getToken()
 
	def setId(self, val):
		x = -1
		for i in xrange(0, len(identifierTable)):
			if identifierTable[i][0] == self.name:
				x = i
		if x >= 0 and identifierTable[x][2] == True:								
			print 'Variable already declared.'
			exit()	
		elif x >= 0 and identifierTable[x][2] == False:								
			identifierTable[x] = identifierTable[x][:1] + (val, False, True)
		elif x < 0 and len(identifierTable) > 0 and identifierTable[0][2] == False:			
			print 'Variable %s was never declared.' % self.name
			exit()
		else:																
			identifierTable.append((self.name, val, True, False))
 
	def execute(self):
		return self.name
 
	def Print(self):
		return self.name
