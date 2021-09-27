S = input()
N = len(S)
ans = 1000
for i in range(N-2):
	tmp = abs(753 -(int(S[i:i+3])))
	ans = min(ans,tmp)
print(ans)
