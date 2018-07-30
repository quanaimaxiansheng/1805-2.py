# coding=utf-8
from socket import *   #导入套接字
from threading import Thread,Lock  #导入多线程、锁

s=socket(AF_INET,SOCK_DGRAM)  
#s.bind((" ",8888))
#udpSocket.bind(bindAddr)  #绑定端口号
class w1(Thread):
	def chuan(self):
		while True:
			if lock1.acquire():
				print("自己的内容")
				a=input("请输入内容")
				s.sendto(a.encode("gb2312"),("192.168.56.1",8080))
				lock2.release()
class w2(Thread):
	def jie(self):	
		while True:
			if lock2.acquire():
				print("接收的内容")
				msg=s.recvfrom(1024)
				print("消息是：%s 来自ip：%s"%(msg[0].decode("gb2312"),msg[1][0]))
				lock1.release()


lock1=Lock()

lock2=Lock()
lock2.acquire()

t1=w1()
t2=w2()

t1.start()
t2.start()
s.close()

