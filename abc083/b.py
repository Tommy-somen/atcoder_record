n,a,b = map(int,input().split())
cnt = []
for i in range(1,n+1):
	s = list(map(int,str(i)))
	if  a<=sum(s)<=b:
		cnt.append(i)
print(sum(cnt))
