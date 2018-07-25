listt = []
for i in range(1,4):
	dictt = {}
	name = input("请输入名字")
	age = input("请输入年龄")
	sex = input("请输入性别")
	lx = input("请输入QQ")
	weight = input("请输入体重")
	if i != 1:
		for j in listt:
			if name == j["name"]:
				print("名字重复，请重新输入")
				name = input("输入名字")
	dictt["name"]=name
	dictt["age"]=age
	dictt["sex"]=sex
	dictt["lx"]=lx
	dictt["weight"]=weight
	listt.append(dictt)
print(listt)
 
