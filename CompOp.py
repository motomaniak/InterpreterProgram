import sys
class CompOp:
	def __init__(self, t):
		self.case= 0 
		self.t = t			
 
	def parse(self):
		#check which operator is being used by token number and assign a different case for each
		x = int(self.t.peek())
		if x == 25: #!=
			pass
		elif x == 26: #==
			self.case= 1
		elif x == 27: #<
			self.case= 2
		elif x == 28: #>
			self.case= 3
		elif x == 29: #<=
			self.case= 4
		elif x == 30: #>=
			self.case= 5
		else:
			print "Invalid comparison operator."
			sys.exit()
		self.t.getToken()							
 
	def execute(self):
		return self.case
 
	def Print(self):
		if self.case== 0:
			return '!='
		elif self.case== 1:
			return '=='
		elif self.case== 2:
			return '<'
		elif self.case== 3:
			return '>'
		elif self.case== 4:
			return '<='
		elif self.case== 5:
			return '>='
