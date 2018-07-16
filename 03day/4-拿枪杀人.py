class Person():#人类
	def __init__(self,name):
		self.name = name
		self.hp = 100
		
	def naqiang(self,gun):#持枪
		self.gun = gun

	def zhuangzidan(self,danjia,zidan):
		danjia.list.append(zidan)#装子弹

	
	def zhuangdanjia(self,gun,danjia):#装弹夹
		gun.danjia = danjia

	def openGun(self,diren):#开枪
		zidan = self.gun.danjia.tanzidan()	
		zidan.kill(diren)

	#count--伤害量
	def diaoxue(self,count):
		self.hp -= count
		print("还剩多少%d"%self.hp)
		if self.hp  <= 0:
			print("挂了")


class Gun():#枪类
	def __init__(self,name):
		self.name = name
		self.danjia = None#假设没有弹夹

class DanJia():#弹夹类
	def __init__(self,name,count):
		self.name = name
		self.count = count
		self.list = []#装子弹

	def tanzidan(self):#弹子弹
		zidan = self.list.pop()
		return zidan


class ZiDan():#子弹
	def __init__(self,name,kill_count):
		self.name = name
		self.kill_count = kill_count#子弹伤害

	def kill(self,diren):#子弹杀人
		diren.diaoxue(self.kill_count)
			


laowang = Person("老王")#创建老王
ak47 = Gun("ak47")#创建枪
danjia = DanJia("快速扩容",40)#创建弹夹

laowang.naqiang(ak47)#让老王持枪

for i in range(40):#创建一些子弹
	zidan = ZiDan("5.56",20)
	laowang.zhuangzidan(danjia,zidan)

laowang.zhuangdanjia(ak47,danjia)#装弹夹

laosong = Person("老宋")

laowang.openGun(laosong)
laowang.openGun(laosong)
