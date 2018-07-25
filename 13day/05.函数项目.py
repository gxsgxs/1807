lst = []

def aaa():
	lsy = {}
	name = input("请输入姓名")
	age = int(input("请输入年龄"))
	lsy["name"] = name
	lsy["age"] = age
	lst.append(lsy)
	print("添加成功")

def bbb():
	name = input("输入要查找的姓名")
	for lsy in lst:
		if lsy["name"] == name:
			print("名字:%s\n年龄:%d"%(lsy["name"],lsy["age"]))
			break

def ccc():
	name = input("输入要修改的名字")
	for lsy in lst:
		if lsy["name"] == name:
			print("1修改名字")
			print("2修改年龄")
			num = int(input("选择功能"))
			if num == 1:
				num = input("输入新名字")
				lsy["name"] = name
			elif num == 2:
				num = input("输入新年龄")
				lsy["age"] = age
			print("修改成功")
			break	
aaa()
bbb()
ccc()
