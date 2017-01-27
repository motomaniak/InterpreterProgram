import sys
import Comp
import Cond
class Cond:			
	def __init__(self, t):
		self.case= 0 
		self.t = t
 
	def parse(self):
		#See which token is next and parse accordingly 
		x = int(self.t.peek())
		if x == 20: #(
			self.comp = Comp.Comp(self.t)
			self.comp.parse()
		elif x == 15: #!
			self.case= 1
			self.t.getToken()
			self.cond = Cond.Cond(self.t)
			self.cond.parse()
		elif x == 16: #[
			self.cond = Cond.Cond(self.t)
			self.cond.parse()
			if x == 18: #&&
				self.case= 2
				t.getToken()
				self.cond2 = Cond.Cond(self.t)
				self.cond2.parse()
			elif x == 19: #||
				self.case= 3
				self.t.getToken()
				self.cond2 = Cond.Cond(self.t)
				self.cond2.parse()
			else:
				print "Invalid condition operator. " + str(self.t.peek())
				sys.exit()
			if self.t.getToken() != 17: #]
				print "Expected end square bracket."
				sys.exit()
 
	def execute(self):
		if self.case== 0:
			return self.comp.execute()
		elif self.case== 1:
			return not self.cond.execute()
		elif self.case== 2:
			return self.cond.execute() and self.cond2.execute()
		else:
			return self.cond.execute() or self.cond2.execute()
 
	def Print(self):
		if self.case== 0:
			return self.comp.Print()
		elif self.case== 1:
			return "!" + self.cond.Print()
		elif self.case== 2:
			return '[' + self.cond.Print() + ' && ' + self.cond2.Print() + ']'
		elif self.case== 3:
			return '[' + self.cond.Print() + ' || ' + self.cond2.Print() + ']'
		else:
			print "Impossible."
			sys.exit()
