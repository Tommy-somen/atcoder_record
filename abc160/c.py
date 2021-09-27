k,n = map(int,input().split())
a = list(map(int,input().split()))
l = []
l.append(abs(k-abs(a[0]-a[n-1])))
for i in range(n-1):
	l.append(abs(a[i]- a[i+1]))
print(sum(l)-max(l))
