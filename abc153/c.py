n,k = map(int,input().split())
h = list(map(int,input().split()))
h.sort(reverse = True)
if k > n:
	k = n
for i in range(k):
	h[i] = 0
print(sum(h))
