from socket import *
#创建一个tcp套接字
s = socket(AF_INET,SOCK_STREAM)
#建链接服务器，来做三次握手
s.connect(("192.168.56.1",8080))

content = input("请输入内容")

s.send(content.encode("gb2312"))

while True:
	msg = s.recv(1024)
	print(msg.decode("gb2312"))

