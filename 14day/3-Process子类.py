from multiprocessing import Process
import time
import os
class Process_Class(Process):
	
	def __init__(self,interval):
		Process.__init(self)
		self.interval = interval

	def run(self):
		print("子进程(%s)开始执行，父进程(%s)"%(os.getpid(),os.getppid()))
		t_start = time.time()
		time.sleep(self.interval)
		t_stop = time.time()

		print("(%s)执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))

