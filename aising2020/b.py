n = int(input())
a = list(map(int,input().split()))
cnt = 0
a.insert(0,0)
for i in range(1,n+1,2):
	if a[i]%2 != 0:
		cnt += 1
print(cnt)
