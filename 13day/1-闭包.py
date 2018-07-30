def num(a,b):
	def it(x):
		return a*x+b
	return it
a=num(5,6)
x=int(input("请输入一个数字"))
print(a(x))
