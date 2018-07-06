import random
class tool():
	def __init__(self):
		self.list=[]
		while len(self.list)<10:
			number=random.randint(1,100)
			if number in self.list:
				continue
			self.list.append(number)
		print(self.list)
	def qian(self):
		pass
	def ban(self):
		pass
gj=tool()
