gaoshi=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in gaoshi:
	#print(i)
	for j,k in i.items():
		#print(j,k)
		for l,s in k.items():
			print(j,l,s)
