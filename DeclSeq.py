import sys
import Decl
class DeclSeq:
	def __init__(self, t):
		self.decl = Decl.Decl(t)
		self.isDelSeq = 0
		self.t = t
 
	def parse(self):
		x = int(self.t.peek())
		if x != 4:
			print "int keyword expected."
			sys.exit()
 
		self.decl.parse()
 
		#check if declaration sequence
		x = int(self.t.peek())
		if x == 4:
			self.isDelSeq = 1
			self.declSeq = DeclSeq(self.t)
			self.declSeq.parse()
 
	def execute(self):
		self.decl.execute()
		if self.isDelSeq == 1:
			self.declSeq.execute()
 
	def Print(self):
		self.decl.Print()
		if self.isDelSeq == 1:
			self.declSeq.Print()
