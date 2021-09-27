n,k = map(int,input().split())
ans,cnt = 0,0
for i in range(1,n+1):
	while(i<k):
		i = i*2
		cnt += 1
	ans += (1/n)*(1/2)**cnt
	cnt = 0
print(ans)
