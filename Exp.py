import Fact
class Exp:			
	def __init__(self, t):
		self.f = Fact.Fact(t)
		self.case= 0
		self.t = t
 
	def parse(self):
		self.f.parse()
		#one token look ahead for + or -
 		x = int(self.t.peek())
		if x == 22:
			self.case= 1
			self.t.getToken()						
			self.e = Exp(self.t)
			self.e.parse()
		elif x == 23:
			self.case= 2
			self.t.getToken()						
			self.e = Exp(self.t)
			self.e.parse()
 
	def execute(self):
		#execute plus or minus 
		if self.case== 0:
			return self.f.execute()
		elif self.case== 1:
			return self.f.execute() + self.e.execute()
		elif self.case== 2:
			return self.f.execute() - self.e.execute()
 
	def Print(self):
		returnString = self.f.Print()
		if self.case== 1:
			returnString += " + " + self.e.Print()
		elif self.case== 2:
			returnString += " - " + self.e.Print()
		return returnString
