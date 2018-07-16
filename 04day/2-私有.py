class name():
	def __age(self,age):
		return self.__age
	def __xingge(self,xingge):
		return self.__xingge
	def xingge(self,xingge):
		self.__xingge(xingge)
	def age(self,age):
		self.__age(age)
xxx=input("请输入姓名")
xxx=name()
age=input("请输入年龄")
xingge=input("请输入性格")
xxx.xingge(xingge)
xxx.age(age)
print("年龄：%s\n性格：%s"%(age,xingge))
