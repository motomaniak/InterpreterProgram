import Id
class IdList:		
	def __init__(self, t):
		self.id = None
		self.iList = None
		self.case= 0
		self.t = t
 
	def parse(self):
		self.id = Id.Id(self.t)
		self.id.parse()		
 
		# If the peek token is a comma, then this is a list of identifiers
		x = int(self.t.peek())
		if x == 13:
			self.t.getToken()
			self.case= 1
			self.iList = IdList(self.t)
			self.iList.parse()
 
	def setId(self, val):
		self.id.setId(val)
		if self.case== 1:
			self.iList.setId(val)
 
	def execute(self):
		returnString = self.id.execute()
		if self.case== 1:
			returnString += ',' + self.iList.execute()
		return returnString
 
	def Print(self):
		returnString = self.id.Print()
		if self.case== 1:
			returnString += ", " + str(self.iList.Print())
		return returnString
