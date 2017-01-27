import Int
import Id
import Exp
from MainProgram import identifierTable
class Op:
	def __init__(self, t):
		self.case= 0
		self.t = t
 
	def parse(self):
		# Parse based on one token look ahead
		x = int(self.t.peek())
		if x == 31:
			self.i = Int.Int(self.t)
			self.i.parse()
		elif x == 32:
			self.case= 1
			self.idName = self.t.getValue()
			self.id = Id.Id(self.t)
			self.id.parse()
		elif x == 20:
			self.case= 2
			self.t.getToken()
			self.e = Exp.Exp(self.t)
			x = int(self.t.getToken())
			if x != 21:
				print "Expected end parenthesis."
				exit()
		else:
			print "Invalid op."
			exit()
 
	def execute(self):
		if self.case== 0:
			return self.i.execute()
		elif self.case== 1:
			# Find identifier and check to see if initialized
			x = -1
			for i in xrange(0, len(identifierTable)):
				if identifierTable[i][0] == self.idName:
					x = i
			if identifierTable[x][3] == False:
				print '%s Variable was never initialized.' % identifierTable[x][0]
				exit()
			return identifierTable[x][1]
		else:
			return self.e.execute()
 
	def Print(self):
		if self.case== 0:
			return self.i.Print()
		elif self.case== 1:
			return self.id.Print()
		else:
			return '(' + self.e.Print() + ')'
