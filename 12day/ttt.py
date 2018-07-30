'''
def fib(times):
	n = 0
	a,b = 0,1
	while n<times:
		yield b
		a,b = b,a+b
		n+=1
	return 'done'
f=fib(10)
print(f)
'''
def fib(num):
	a,b = 0,1
	for i in range(num):
	
		a,b = b,a+b
		yield b
f= fib(10)
print(f)
