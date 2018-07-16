class dian():
	def __init__(self,name,ji):
		self.name=name
		self.ji=ji
		self.list=[]
	def __str__(self):
		xinxi=(">单位名称：%s \n>单位级别%s"%(self.name,self.ji))
		return xinxi
class vip():
	def __init__(self):
		self.del={}

	def __str__(self):
		pass
	def add(self):
		pass
	def pop(self):
		pass
	def gai(self):
		pass
	def cha(self):
		pass
	def tui(self):
		pass
class caidan():
	def __init__(self):
		self.kehu=vip()
	def prt(self) :
		print("*"*50)
		print("欢迎使用【名片管理】系统")
		while True:
			fun=int(input("请选择功能：1.加 2.查 3.改 4.删 5.退"))
			if fun==1:
				name=input("请输入姓名")
				sex=input("请输入性别")
				hao=input("请输入编号")
				
				
#创建dian的实例对象
name=input("请输入单位名字")
ji=input("请输入级别")
xxx=dian(name,ji)
print(xxx)
#创建vip类的实例对象
kehu=vip()
