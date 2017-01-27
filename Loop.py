import Cond
import StmtSeq
class Loop:			
	def __init__(self, t, inData):
		self.c = Cond.Cond(t)
		self.stsq = StmtSeq.StmtSeq(t, inData)
		self.t = t
 
	def parse(self):
		x = int(self.t.getToken())
		if x != 8:
			print "while keyword expected."
			exit()
 
		self.c.parse()
 		x = int(self.t.getToken())
		if x != 9:
			print "loop keyword expected."
			exit()
 
		self.stsq.parse()
 		x = int(self.t.getToken())
		if x != 3:
			print "end keyword expected"
			exit()
		x = int(self.t.getToken())
		if x != 12:
			print "Missing semicolon."
			exit()
 
	def execute(self):
		while self.c.execute() == 1:
			self.stsq.execute()
 
	def Print(self):
		return "while " + self.c.Print() + " loop\n	" + self.stsq.Print() + "\n	end;"
