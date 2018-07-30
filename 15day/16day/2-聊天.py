from socket import *
from threading import Thread

s=None
ip=""
port=0

def read():
	while True:
		content = input("请输入内容")
		s.sendto(content.encode("gb2312"),(ip,port))



def shou():
	while True:
		msg = s.recvfrom(1024)
		print(msg[0].decode("gb2312"))
		



def main():
	global s
	global ip
	global port
	port = int(input("请输入对方端口:"))
	ip = input("请输入对方IP:")
	s = socket(AF_INET,SOCK_DGRAM)
	#s.bind(("",8888))
	
	t = Thread(target=read)
	t1= Thread(target=shou)
	
	t.start()
	t1.start()

	t.join()
	t1.join()

if __name__=="__main__":
	main()
