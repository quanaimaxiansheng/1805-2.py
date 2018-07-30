from multiprocessing import Process
import time

def w():
	for i in range(5):
		time.sleep(1)
		print("lalala")
a = Process(target=w)
a.start()
a.join()
print("好啦")
