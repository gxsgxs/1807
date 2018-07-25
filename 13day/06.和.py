def test(a,*args,b=12,**kwargs):
	sum = 0
	sum = sum+a
	for i in args:
		sum+=i
	sum = sum+b
	for j,k in kwargs.items():
		sum+=k
	print(sum)
	

test(1,2,3,4,5,b=20,m=12,n=22)
	

