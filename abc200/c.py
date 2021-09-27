from collections import deque

n = int(input())

A = list(map(int,input().split()))

NumList = [deque() for x in range(200)]
cnt = 0

for i in A:
  tmp = int(i%200)
  NumList[tmp].append(i)

for k in NumList:
  l = len(k)
  cnt += (l*(l-1))//2
  
print(cnt)
