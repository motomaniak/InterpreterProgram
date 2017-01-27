import Exp
import Id
from MainProgram import identifierTable
class Assign:		
	def __init__(self, t):
		self.e = Exp.Exp(t)
		self.id = Id.Id(t)
		self.t = t
 
	def parse(self):
		x = int(self.t.peek())
		if x != 32:
			print "Identifier expected."
			exit()
 
		self.id.parse()
 		x = int(self.t.getToken())
		if x != 14:
			print "= expected."
			exit()
 
		self.e.parse()
 		x = int(self.t.getToken())
		if x != 12:
			print "Semicolon expected."
			exit()
 
	def execute(self):
		# Check if the identifier is already in the table and then update its value if it is
		x = -1
		for i in xrange(0, len(identifierTable)):
			if identifierTable[i][0] == self.id.execute():
				x = i 
		if x >= 0:
			self.id.setId(self.e.execute())
		else:
			print 'Identifier must be declared in declaration sequence.'
			exit()
 
	def Print(self):
		return self.id.Print() + " = " + self.e.Print() + ";"
