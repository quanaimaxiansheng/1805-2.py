from multiprocessing import Manager,Pool
import time

def cun(q):
	for i in range(5):
		time.sleep(1)
		q.put("取走%d"%i)
		print("存储%d"%i)

def qu(q):
	while Ture:
		if q.empty() == False:
			for i in range(q.qsize()):
				time.sleep(1)
				print(q.get())

p = Pool()
q = Manager().Queue()
p.apply_async(cun,(q,))
p.apply_async(qu,(q,))
p.close()
p.join()
