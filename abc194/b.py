n = int(input())
x = [list(map(int,input().split())) for _ in range(n)]

same = []
diff = []

for i in x:
	same.append(i[0]+i[1])

for j in range(0,n):
	for k in range(0,n):
		if j == k:
			pass
		else:
			diff.append(max(x[j][0],x[k][1]))

ans = min(min(same),min(diff))
print(ans)
