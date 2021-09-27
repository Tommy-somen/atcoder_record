N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
sub = []
ans = 0
for i in range(N):
	sub.append(V[i] - C[i])

for j in range(N):
	if sub[j] > 0:
		ans += sub[j]
print(ans)
