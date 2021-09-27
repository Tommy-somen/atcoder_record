N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(0,N-1):
  for j in range(1,N):
    tmp = abs(A[i] - A[j])
    cnt = max(cnt,tmp)
print(cnt)
           
    
