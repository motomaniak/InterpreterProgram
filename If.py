import Cond
import StmtSeq

class If:			
	def __init__(self, t, inData):
		self.c = Cond.Cond(t)
		self.stsq = StmtSeq.StmtSeq(t, inData)
		self.case= 0
		self.t = t
		self.inData = inData
 
	def parse(self):
		x = int(self.t.getToken())
		if x != 5:
			print "if keyword expected."
			exit()
 
		self.c.parse() 
 		x = int(self.t.getToken())
		if x != 6:
			print "then keyword expected."
			exit()
 
		self.stsq.parse()
 
		# Check if there is an else
		x = int(self.t.peek())
		if x == 7:
			self.case= 1
			self.t.getToken() 								
			self.stsq2 = StmtSeq.StmtSeq(self.t, self.inData)
			self.stsq2.parse()
 		x = int(self.t.getToken())
		if x != 3:
			print 'end keyword expected.'
			exit()
		x = int(self.t.getToken())
		if x != 12:
			print 'Missing semicolon.'
			exit()
 
	def execute(self):
		if self.case== 0:
			if self.c.execute():
				self.stsq.execute()
		else:
			if self.c.execute():
				self.stsq.execute()
			else:
				self.stsq2.execute()
 
	def Print(self):
		returnString = "if " + self.c.Print() + " then\n\t	" + self.stsq.Print()
		if self.case== 1:
			returnString += "\n\t	else\n\t	" + self.stsq2.Print()
		returnString += "\n\t	end;"
		return returnString
