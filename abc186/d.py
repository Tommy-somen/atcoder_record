n = int(input())
a = list(map(int,input().split()))

a.sort()

ans = 0
total = 0

for i in range(n-1):
  total += a[i]
  ans += abs(total-a[i+1]*(i+1))
  
print(ans)
