N = int(input())
A = list(map(int,input().split()))
A = sorted(A,reverse = True)
A.insert(N,0)
ans = 0
for i in range(0,N,2):
	ans += (A[i] - A[i+1])
print(ans)
