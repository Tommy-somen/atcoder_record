import sys
from collections import deque
n,y = list(map(int,input().split()))

ans = deque()

for i in range(0,n+1):
  for j in range(0,n+1):
    value = y - (1000*i + 5000*j)
    if value >= 0:
      if (value%10000 == 0) and ((value//10000)+j+i == n):
        ans.append([(value//10000),j,i])

for d in ans:
  if y == d[0]*10000 + d[1]*5000 + d[2]*1000:
    if n == d[0] + d[1] + d[2]:
      print(*d)
      sys.exit()

wrong = [-1,-1,-1]
print(*wrong)
