g = 77
def test():
	global g
	g = 777
	print(g)
print(g)
test()
