account = "123456"
password = "888888"

act = input("请输入账户")
paswd = input("请输入密码")
if act == account and paswd == password:
	print("登录成功")
elif act != account:
	print("账户错误")
elif paswd != password:
	print("密码错误")
