lists=[]
while True:
	print("                   《欢迎来到学生管理系统》              ")
	print("1,添加学生信息")
	print("2,查找学生信息")
	print("3,修改学生信息")
	print("4,删除学生信息")
	print("5,退出学生信息")
	sh=int(input("选择所需选项"))

	if sh==1:
		mz=input("输入名字:")
		nl=input("输入年龄:")
		xb=input("输入性别:")
		dz=input("输入地址:")
		d={}
		d["name"]=mz
		d["age"]=nl
		d["sex"]=xb
		d["dz"]=dz
		lists.append(d)
		print(lists)

	elif sh==2:
		a=input("输入查找的联系人")
		for i in lists:
			if a==i["name"]:
				print("学生姓名:%s\n学生年龄:%s\n学生性别:%s\n学生家庭地址:%s"%(i["name"],i["age"],i["sex"],i["dz"]))
				break
	elif sh==3:
		b=input("输入要修改的信息姓名:")
		for i in lists:
			if b==i["name"]:
				print("学生姓名:%s\n学生年龄:%s\n学生性别:%s\n学生家庭地址:%s"%(i["name"],i["age"],i["sex"],i["dz"]))
			print("1:修改名字")
			print("2:修改年龄")
			print("3:修改性别")
			print("4:修改家庭住址")
			num = int(input("选择修改项"))
			if num == 1:
				name = input("请输入新的名字")
				i["name"] = name
			elif num == 2:
				age = int(input("请输入新的年龄"))
				i["age"] = age
			elif num == 3:
				sex = input("请输入新的性别")
				i["sex"] = sex
			elif num == 4:
				dz = input("请输入新的地址")
				i["dz"] = dz
				break
			print("修改成功")
			print(lists)

	elif sh==4:
		e=input("输入要删除的内容:")
		for n in lists:
			if e==n["name"]:
				lists.remove(n)
				print(lists)
	elif sh==5:
		print("                      谢谢使用O(∩_∩)O~                  ")
		break
