a,b,n = map(int,input().split())
if n >= b:
	n = b-1
	print((a*n)//b - ((n//b)*a))
else:
	print((a*n)//b - ((n//b)*a))
	
