class student():#创建学生类
	def __init__(self,name,sex):#默认属性
		self.name=name
		self.sex=sex
	def upclass(self):
		print("上课")
	def __str__(self):
		return '我的名字是：%S \n我的性别是%s'%(self.name,self.sex)



class manager():#创建管理方法类
	def __init__(self,student):
		self.list=[] #用来装学生的信息
	def add(self,student):
		self.list.append(student)
		for i in self.list:
			print(i)
	def cha(self):
		pass
	def gai(self):
		pass
	def pop(self):
		pass
	def tui(self):	
		pass

class menu():#创建菜单类
	def __innit__(self):
		self.m=manager() #让菜单类持有管理对象的引用
	def print_men(self):
		print("欢迎使用学生管理系统")
		while Ture:
			fun=int(input("请选择功能：1.增 2.查 3.改 4.删 5.退"))
			fun ==1:
				name=input("请输入名字")
				sex=input("请输入性别")
				s=student(name,sex)
				self.m.add(s)


m=menu()
m.print_men()


