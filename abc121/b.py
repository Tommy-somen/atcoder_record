N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for n in range(N)]
sum,count = 0,0

for i in range(N):
	for j in range(M):
		sum += A[i][j]*B[j]
	if sum+C > 0:
		count += 1
	sum = 0
print(count)
