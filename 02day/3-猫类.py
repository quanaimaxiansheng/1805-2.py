class cat():
	def eat(self,a):
		print("我吃%s"%a)
	def zuo(self):
		print("抓老鼠")
	def introduce(self):
		print("我的颜色是%s  我的价格是%d"%(self.color,self.price))
pinzhong=int(input("请输入品种:1.加菲猫 2.波斯猫"))
name=cat()
if pinzhong == 1:
	
	a=input("请输入食物")
	
	name.eat(a)
	name.color="条纹相间"
	name.price=100
	name.introduce()
	
elif pinzhong == 2:
	
	a=input("请输入食物")
	
	name.eat(a)
	name.color="屎一样的黄"
	name.price=300
	name.introduce()
