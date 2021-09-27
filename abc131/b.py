N,L = map(int,input().split())
taste = []
tmp = []
for i in range(1,N+1):
	tmp.append(abs(L + i -1))
	taste.append((L + i -1))
num = tmp.index(min(tmp)) 
taste[num] = 0
print(sum(taste))
