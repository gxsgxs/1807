x = float(input("输入一个数值"))
y = float(input("输入一个数值"))
z = input("+-*/")


if z == "+":
	print(x+y)
elif z == "-":
	printx-y
elif z == "*":
	print(x*y)
elif z == "/":
	if y == 0:
		print("不合法")
	else:
		print(x/y)
