'''
gxs = []
for i in range(1,101):
	if i % 2 == 0:
		gxs.append(i)
print(gxs)
gxs.remove(20)
gxs.pop(1)
print(gxs)
'''

gxs = []
i = 1
while i < 101:
	if i%2 == 0:
		gxs.append(i)
	i+=1
print(gxs)
gxs.remove(20)
gxs.pop(1)
print(gxs)
