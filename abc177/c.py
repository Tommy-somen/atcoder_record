n = int(input())
a = list(map(int,input().split()))

sum_a = sum(a)
total = 0

for i in range(n-1):
  mul = a[i]
  sum_a -= a[i]
  total += (sum_a*mul)
  total %= (10**9+7)
  
print(total)
