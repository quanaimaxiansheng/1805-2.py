class su():

	def shu(self):
		for i in range (100,201):
			falg = True
			for j in range(2,i):
				if i%j ==0:
					falg = False
					break
			if falg==True:
			 
				print(i)
a=su()
a.shu()
