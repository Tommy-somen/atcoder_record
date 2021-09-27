N = int(input())
s = [input() for s in range(N)]
M = int(input())
t = [input() for t in range(M)]
ans = 0
for i in range(N):
	tmp = s.count(s[i]) - t.count(s[i])
	ans = max(ans,tmp)
print(ans)
