n = int(input())
x = list(map(int,input().split()))
ans= []
for i in range(max(x)+1):
	tmp = 0
	for j in range(n):
		tmp += (x[j]-i)**2
	ans.append(tmp)
print(min(ans))
