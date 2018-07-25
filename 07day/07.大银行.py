account = "777777"
password = "999999"
money = 888888888

ount = input("请输入一个账号")
word = input("请输入一个密码")
if ount == account and word == password:
	print("可以取钱")
	oney = float(input("请输入取钱金额"))
	ey = money-oney
	if oney > money:
		print("没钱取毛线")
	else: 
		print (ey)
else:
	print("非法账户") 
