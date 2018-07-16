class yi():
	def __init__(self,a,b):
		self.num=a
		self.num1=b
	def add(self):
		print("%d+%d=%d"%(self.num,self.num1,self.num+self.num1))
	def jian(self):
		print("%d-%d=%d"%(self.num,self.num1,self.num-self.num1))
	
	def cheng(self):
		print("%d*%d=%d"%(self.num,self.num1,self.num*self.num1))
		

	def chu(self):
		print("%d/%d=%d"%(self.num,self.num1,self.num/self.num1))
try:	
	
	a=int(input("请输入数字"))
	b=int(input("请输入数字"))
	
except Exception as ret:
	
	print("出错了，错误为：%s"%ret)
else:
	ma=yi(a,b)
	ma.add()
	ma.jian()
	ma.cheng()
	while True:
		if b==0:
			print("此数值不能为0")
			break
		else:
			ma.chu()
			break
	

