class ren():
	def man(self):
		print("男人")
	def fiman(self):
		print("女人")
	def sss(self):
		print("很难")
	def s(self):
		print("好看")
	def gn(self):
		print("吃喝")
	def gn1(self):
		print("拉撒")
	def gn2(self):
		print("睡")
	def gn3(self):
		print("干")
name=input("请输入姓名")
name=ren()
sex=int(input("1.男人  2.女人"))
if sex==2:
	name.s()
	name.gn()
	name.gn2()
elif sex==1:
	name.sss()
	name.gn1()
	name.gn3()
	
