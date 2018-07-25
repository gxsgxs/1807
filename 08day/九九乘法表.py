i=0
while i<10:
	row=1
	while row <=i:
		print("%d*%d=%2d"%(row,i,i*row),end = "  ")
		row+=1
	print(" ")
	i+=1
