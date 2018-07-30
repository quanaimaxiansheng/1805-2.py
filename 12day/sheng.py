def test(num):
	a,b=0,1
	for i in range(num):
		print(b)
		yield b
	
		a,b=b,a+b
g=test(8)
print(g)		
	
