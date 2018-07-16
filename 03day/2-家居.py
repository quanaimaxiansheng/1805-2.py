#房子的类
class home():
	def __init__(self,name,dizhi,mianji):
		self.dizhi=dizhi
		self.mianji=mianji
		self.name=name
		self.list=[]
	def __str__(self):#返回实例对象
		return "%s的家 地址：%s 面积：%d"%(self.name,self.dizhi,self.mianji)
	def addjiaju(self,jiaju):
		if self.mianji < jiaju.size:
			print("面积不足，装不下了")
		else:
			self.list.append(jiaju)
			self.mianji -= jiaju.size
	def tell(self):
		return self.mianji
#家居的类
class ju():
	def __init__(self,name,yang,size):
		self.name=name
		self.yang=yang
		self.size=size

	def __str__(self):
		return "家居的名字：%s 规格：%s 大小：%d"%(self.name,self.yang,self.size)
#家
name=input("请输入姓名")
a=input("请输入地址")
b=int(input("请输入面积"))
jia=home(name,a,b)
print(jia)
#家居
while True:
	jname=input("请输入家居的名字")
	yang=input("请输入规格")
	size=int(input("请输入大小"))
	jiaju=ju(jname,yang,size)
	print(jiaju)
	list=jia.addjiaju(jiaju)	
	print(jia.list)
