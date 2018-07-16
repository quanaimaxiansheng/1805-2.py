class nan():
	def eat(self):
		print("吃食物")
	def sleep(self):
		print("睡觉")


class nv():
	def wan(self):
		print("打豆豆")
		



class er(nan,nv):
	pass
'''
	def nam(self,name):
		print("姓名是：%s"%self.name)
'''

name=input("请输入姓名")
a=er()
a.eat()
a.sleep()
a.wan()
