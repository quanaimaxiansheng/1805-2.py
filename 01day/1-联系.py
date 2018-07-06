'''
name=input("请输入要备份的名字")
f=open(name,'r')
while True:
	if f.read(1024) == "":
		break
content=f.read()
a=name.rfind('.')
newname=name[:a]+"back"+name[a:]


f1=open(newname,'w')
f1.write(content)
f.close()
f1.close()
'''
name=input("请输入你要备份的文件名")
f=open(name,'r')
a=f.read()
position=name.rfind(".")
new_name=name[:position]+"back"+name[position:]
s=open(new_name,"w")
s.write(a)
f.close()
s.close()
