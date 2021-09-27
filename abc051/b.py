k,s = map(int,input().split())
cnt,x = 0,0
for y in range(k+1):
	for z in range(k+1):
		x = s-y-z
		if 0 <= x <= k:
			cnt += 1
print(cnt)
