class ren():
	def __init__(self,name,hight,wight):
		self.name=name
		self.hight=hight
		self.wight=wight
	def introduce(self):
		print("姓名：%s 身高：%d 体重：%d "%(self.name,self.hight,self.wight))

while True:

	name=input("请输入名字")
	hight=int(input("请输入身高"))
	wight=int(input("请输入体重"))

	people=ren(name,hight,wight)

	people.introduce()

		
	
	
