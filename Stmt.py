import If
import Loop
import Input
import Output
import Assign
class Stmt:
	def __init__(self, t, inData):
		self.case= 0
		self.t = t
		self.inData = inData
 
	def parse(self):	
		x = int(self.t.peek())	
		if x == 5:
			self.st = If.If(self.t, self.inData) 
			self.st.parse()
		elif x == 8:
			self.case= 1
			self.st = Loop.Loop(self.t, self.inData)
			self.st.parse()
		elif x == 10:
			self.case= 2
			self.st = Input.Input(self.t, self.inData)
			self.st.parse()
		elif x == 11:
			self.case= 3
			self.st = Output.Output(self.t)
			self.st.parse()	
		elif x == 32:
			self.case= 4
			self.st = Assign.Assign(self.t)
			self.st.parse()
		else:
			print "Something went wrong!."
			exit()
 
	def execute(self):
		self.st.execute()
 
	def Print(self):
		return self.st.Print()
