import Op

class Fact:			
	def __init__(self, t):
		self.case= 0
		self.o = Op.Op(t)
		self.t = t
 
	def parse(self):
		self.o.parse()
 		x = int(self.t.peek())
		if x == 24:
			self.case= 1
			self.t.getToken() 					
			self.f = Fact(self.t)
			self.f.parse()
 
	def execute(self):
		if self.case== 1:
			return self.o.execute() * self.f.execute()
		else:
			return self.o.execute()
 
	def Print(self):
		returnString = self.o.Print()
		if self.case== 1:
			returnString += ' * ' + self.f.Print()
		return returnString
