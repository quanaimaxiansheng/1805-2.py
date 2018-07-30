def w(type):
	def w1(fun):
		def inner():
			if type == 1:
				print("验证吃鸡账号")
			elif type == 2:
				print("验证王者账号")
			fun()
		return inner
	return w1

@w1
def play():
	print("我要玩吃鸡")

@w2
def play1():
	print("我要玩王者")


play()
play1()
