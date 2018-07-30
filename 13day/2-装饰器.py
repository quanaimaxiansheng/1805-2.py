def w1(fun):
	def nn(*args,**kwargs):
		print("XXX")
		return fun(*args,**kwargs)
		
	return nn


@w1
def test():
	print("YYY")
test()


@w1
def test1(a):
	print("哈哈%s"%a)
test1("呵呵")


@w1
def test3():
	return "臭不要脸"
xxx=test3()
print(xxx)


@w1
def test4(b):
	return "臭嗨"
yyy=test4("lao")
print(yyy)

