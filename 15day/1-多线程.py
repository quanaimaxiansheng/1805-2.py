from threading import Thread,Lock
import time
num = 0
'''
#第一种可以解决问题，但是改成了单任务，不可取
flag=1
def w1():
	global num
	global flag
	if flag == 1:
		for i in range(1000000):
			num += 1
		flag = 2
	print("线程一%d"%num)

def w2():
	global num
	while True:
		if flag == 2:
			for i in range(1000000):
				num += 1
			break
	print("线程二%d"%num)
'''
def w1():
	global num
	for i in range(100000000):
		mutex.acquire(True) #阻塞
		num += 1
		mutex.release() #释放锁
	print("线程一%d"%num)

def w2():
	global num
	for i in range(100000000):
		mutex.acquire(True)
		num += 1
		mutex.release()
	print("线程二%d"%num)

mutex = Lock()

w1= Thread(target=w1)
w2 = Thread(target=w2)
w1.start()
w2.start()
