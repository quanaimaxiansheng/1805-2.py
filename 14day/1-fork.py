import os
import time

num = 1
p = os.fork()

if p == 0:
	print("我是子进程")
	time.sleep(2)
	print("我是子进程num = %d"%num)

else:
	num += 1
	print("我是父进程num = %d"%num) 
