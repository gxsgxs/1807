def gxs():

	import random
	l = []
	for i in range(1,100):
		n = random.randint(1,100)
		if i != 1:
			if l.count(n) == 1:
				n = random.randint(1,100)	
		l.append(n)
	print(l)

gxs()
