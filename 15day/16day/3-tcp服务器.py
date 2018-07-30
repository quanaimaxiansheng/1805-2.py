from socket import *
#A_INET ipv4

s=socket(AF_INET,SOCK_STREAM)

#s.bind(("",8889))

s.listen(3)
print("--1--")

client,address = s.accept()
print("--2--")	
msg = client.recv(1024)

print(msg.decode("gn2312"))

a = input("请输入要回复：")
client.send(a.encode("gb2312"))
	
client.close()

s.close()
