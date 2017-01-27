import sys

class Int:			
	def __init__(self, t):
		self.val = 0
		self.t = t
 
	def parse(self):
		x = int(self.t.peek())
		if x != 31:
			print "Not a valid integer."
			sys.exit()
 
		self.val = self.t.getValue()
		self.t.getToken()				
 
	def execute(self):
		return int(self.val)
 
	def Print(self):
		return str(self.val)
