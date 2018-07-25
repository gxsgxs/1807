#coding=utf-8
account = "gxs"
password = "888888"
i = 0
while True:
	ount = input("请输入账号:")
	word = input("请输入密码:")
	if ount == account and word == password:
		print("登陆成功")
		number = int(input("0:adc 1:肉 3:法师"))
		if number == 0:
			print("鲁班大师")
		elif number == 1:
			print("程咬金")
		elif number == 3:
			print("王昭君")
	else:
		print("已经%d次错误"%i)
	i+=1
	if i == 4:
		print("账号以冻结")
		break

