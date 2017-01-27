import sys
import DeclSeq
import StmtSeq
import pdb
from MainProgram import identifierTable
class Program:		
	def __init__(self, t, inData):
		self.ds = DeclSeq.DeclSeq(t)
		self.ss = StmtSeq.StmtSeq(t, inData)
		self.t = t
 
	def parse(self):
		x = int(self.t.getToken())
		if x != 1:
			print "program keyword expected."
			sys.exit()
 
		self.ds.parse()
 		x = int(self.t.getToken())
		if x != 2:
			print "begin keyword expected."
			sys.exit()
 
		self.ss.parse()
 		x = int(self.t.getToken())
		if x != 3:
			print "end keyword expected."
			sys.exit()
 
	def execute(self):
		self.ds.execute()
		#update identifierTable
		for i in xrange(0,len(identifierTable)):
			identifierTable[i] = identifierTable[i][:2] + (False, False)
 
		self.ss.execute()
 
	def Print(self):
		print "program"
		self.ds.Print()
		print "begin"
		print self.ss.Print()
		print "end"
 
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"
