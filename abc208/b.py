import math

p = int(input())

coin = [math.factorial(1),math.factorial(2),math.factorial(3),math.factorial(4),math.factorial(5),math.factorial(6),math.factorial(7),math.factorial(8),math.factorial(9),math.factorial(10)]
#print(coin)
ans = 0

for i in range(9,-1,-1):
  if p >= coin[i]:
    ans += (p//coin[i])
    p -= coin[i]*(p//coin[i])
    
print(ans)
