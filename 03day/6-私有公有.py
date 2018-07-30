class wo():
	def __init__(self,mimi):
		self.__mimi = mimi
	def getmimi(self):
		return self.__mimi
mimi=input("请输入你的秘密")
yuxing=wo(mimi)
print(yuxing.getmimi())

