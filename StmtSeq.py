import Stmt
import pdb
class StmtSeq:		
	def __init__(self,t, inData):
		self.st = Stmt.Stmt(t, inData)
		self.case= 0
		self.t = t
		self.inData = inData
 
	def parse(self):
	
		if self.t.isStmt():
			x = int(self.t.peek())
			if x in [5,8,10,11,32]:
				self.st.parse()
			else:
				print "There was an unintended error!"
				exit()
				self.st.parse()
		else:
			print "Expected valid statement token. Found %s" % self.t.peek()
			#exit()
 
		# Check if the following token is a StmtSeq
		if self.t.isStmt():
			self.case= 1
			self.stsq = StmtSeq(self.t, self.inData)
			self.stsq.parse()			
 
	def execute(self):
		self.st.execute()
		if self.case== 1:
			self.stsq.execute()
 
	def Print(self):
		returnS = "	" + self.st.Print()
		if self.case== 1:
			returnS += "\n" + self.stsq.Print()
		return returnS
