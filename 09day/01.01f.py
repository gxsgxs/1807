import random
shu = random.randint(1,100)
for i in range(1,10):
	poshu = int(input("请输入一个数"))	
	if poshu < shu:
		print("小了")
	elif poshu > shu:
		print("大了")
	elif poshu == shu:
		print("牛逼")
		break
print("游戏结束")
