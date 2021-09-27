n = int(input())

tani = [10**3,10**6,10**9,10**12,10**15]

cnt = 0

for i in range(5):
	s = n - tani[i]
	if s >= 0:
		cnt += s+1
	else:
		break
print(cnt)
