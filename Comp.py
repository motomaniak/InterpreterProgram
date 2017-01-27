import Op
import CompOp
class Comp:			
	def __init__(self, t):
		self.op1 = Op.Op(t)
		self.cOp = CompOp.CompOp(t)
		self.op2 = Op.Op(t)
		self.t =t 
 
	def parse(self):
		x = int(self.t.getToken())
		if x != 20:
			print "Open parenthesis expected."
			exit()
 
		self.op1.parse()
		self.cOp.parse()
		self.op2.parse()
 		x = int(self.t.getToken())
		if x != 21:
			print "Closed parenthesis expected."
			exit
 
	def execute(self):
		# Lookup the compare operater and compare the two statemtns 
		compOp = self.cOp.execute()
		truth = 0
		if compOp == 0:
			if self.op1.execute() != self.op2.execute():
				truth = 1
		elif compOp == 1:
			if self.op1.execute() == self.op2.execute():
				truth = 1
		elif compOp == 2:
			if self.op1.execute() < self.op2.execute():
				truth = 1
		elif compOp == 3:
			if self.op1.execute() > self.op2.execute():
				truth = 1
		elif compOp == 4:
			if self.op1.execute() <= self.op2.execute():
				truth = 1
		else:
			if self.op1.execute() >= self.op2.execute():
				truth = 1
		return truth
 
	def Print(self):
		return '(' + self.op1.Print() + ' ' + self.cOp.Print() + ' ' + self.op2.Print() + ')'
 
