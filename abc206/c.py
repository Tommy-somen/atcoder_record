import collections
n = int(input())
A = list(map(int,input().split()))

c = collections.Counter(A)

probably = n

cnt = 0

for i in range(n-1):
  probably -= 1
  if c[A[i]] > 0:
    c[A[i]] -= 1
  cnt += probably - c[A[i]]
  
print(cnt)
