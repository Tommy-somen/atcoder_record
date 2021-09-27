N,M = map(int,input().split())
A = list(map(int,input().split()))
count = 0
for i in range(0,M):
	count += A[i]
print(N-count if N-count >= 0 else "-1")
