import random
num = random.randint(1,100)
for i in range (1,11 ):
	bunum = int(input("请输入一个数字"))
	if bunum < num:
		print("小了")
	elif bunum > num:
		print("大了")
	elif bunum == num:
		print("牛逼")
		break
