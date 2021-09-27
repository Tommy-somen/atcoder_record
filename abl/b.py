a,b,c,d = list(map(int,input().split()))

flg = False
	
if (c <= a <= d) or (c <= b <= d) or (a <= c <= b) or (a <= d <= b):
	flg = True

if flg:
	print('Yes')
else:
	print('No')
