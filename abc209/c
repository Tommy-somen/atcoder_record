n = int(input())
c = list(map(int,input().split()))

c.sort()

multiple = c[0]
ans = c[0]

for i in range(1,n):
  multiple -= 1
  if c[i] - c[i-1] > 0:
    multiple += (c[i] - c[i-1])

  ans *= multiple
  ans %= (10**9+7)
  
print(ans)
