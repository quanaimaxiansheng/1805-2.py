import time
class kao():
	def __init__(self):
		self.zhuangtai="生的"
		self.time=0
		self.list=[]
	def cook(self):
		self.time+=1
		if self.time<5:
			self.zhuangtai='生的'
		elif self.time>=5 and self.time<10:
			self.zhuangtai='半生不受'
		elif self.time>=10 and self.time<15:
			self.zhuangtai='熟啦'
		elif self.time>=15:
			self.zhuangtai='焦成炭了'
	def tell(self):
		print(self.zhuangtai)
		print("佐料有%s"%str(self.list))
	def add(self,a):
		self.list.append(a)
digua=kao()
for i in range(13):
	digua.cook()
	if i==5:
		digua.add("盐")
	digua.tell()
