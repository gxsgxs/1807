lsits = []
while True:
	print("-"*45)
	print("            欢迎来到学生系统         ")
	print("1:添加学生信息:")
	print("2:查找学生信息:")
	print("3:修改学生信息:")
	print("4:删除学生信息:")
	print("5:退出学生系统:")
	num = int(input("选择功能"))
	if num == 1:
		name = input("输入名字")
		age =int(input("输入年龄"))
		sex = input("输入性别")
		d = {}
		d["name"] = name
		d["age"] = age
		d["sex"] = sex
		lsits.append(d)
		print(lsits)
	elif num == 2:
		name = input("请输入学生名字")
		for j in lsits:
			if j ["name"] == name:
				print("学生名字:%s\n学生年龄:%d\n学生性别:%s"%(j["name"],j["age"],j["sex"])) 
				break
	elif num == 3:

		name = input("请输入学生名字")
		for j in lsits:
			if j ["name"] == name:
				print("学生名字:%s\n学生年龄:%d\n学生性别:%s"%(j["name"],j["age"],j["sex"])) 

				print("1:修改姓名")
				print("2:修改年龄")
				print("3:修改性别")
				num = int(input("选择修改项"))
				if num ==1:
					name = input("请输入新的名字")
					j["name"] = name
				elif num ==2:
					age = int(input("请输入新的年龄"))
					j["age"] = age
				elif num == 3:
					sex = input("请输入性别")
					j["sex"] = sex
				print("修改成功")
				break
