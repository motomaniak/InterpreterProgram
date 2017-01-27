import IdList
class Decl:
	def __init__(self, t):
		self.iList = IdList.IdList(t)
		self.t = t
 
	def parse(self):
		self.t.getToken()
		self.iList.parse()
		x = int(self.t.getToken())
		if x != 12:
			print "Semicolon expected."
			exit()
 
	def execute(self):
		# Set the initial value of the variable to None
		self.iList.setId(None)
 
	def Print(self):
		print "	int " + self.iList.Print() + ";"
