class farther():	
	def Zqian(self):
		print("搬砖")
class son(farther):
	def Zqian(self):
		print("写代码")
class Sson(son):
	def Zqian(self):
		print("靠脸")
a=farther()
b=son()
c=Sson()
a.Zqian()
b.Zqian()
c.Zqian()
