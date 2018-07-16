import random 
class a():

	def dian(self):
		cup=random.randint(1,10)
		print("电脑的数字是%d"%cup)
	
		i=0
		while True:
			py=random.randint(1,10)
			if py > cup:
				print("猜大了")
				print("猜的数字是%d"%py)
			elif py < cup:
				print("猜小了")
				print("猜的数字是%d"%py)
			else:
				print("猜的数字是%d"%py)
				print("猜对了")
				break
			i+=1
			if i<3:
				print("大神")
			elif i<6:
				print("学霸")
			elif i<10:
				print("一般")
			else:
				print("你真菜")
wanjia=a()
wanjia.dian()

