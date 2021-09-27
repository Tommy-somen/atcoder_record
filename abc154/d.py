n,k = list(map(int,input().split()))
p = list(map(int,input().split()))

for i in range(n):
  p[i] = ((p[i]*(p[i]+1))//2)/p[i]

kbox = p[:k]

cmp = sum(kbox)
ans = cmp

for j in range(1,n-k+1):
  cmp -= p[j-1]
  cmp += p[j+k-1]
  ans = max(ans,cmp)
  
print(ans)
