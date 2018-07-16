class tool():

	count=0
	def __init__(self,name):
		self.name=name
		tool.count+=1	
	
	def gongju(self):
		
		print("你的购物车中商品:%s"%self.name)
	
	@classmethod
	def getcount(cls):
		return cls.count
		print("购物车个数：%d"%cls.count)
		count+=1


print("网上购物".center(50,"*"))
while  True:
	
	name=input("请输入要购买的工具")
	ming=tool(name)
	ming.gongju()
	print(ming.getcount())

