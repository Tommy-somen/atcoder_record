import sys

n = int(input())
a = list(map(int,input().split()))
x = int(input())

total = sum(a)
base = (x//total)*n

cmp = total*(x//total)
for i in range(n):
  #print(cmp)
  cmp += a[i]
  base += 1
  if cmp > x:
    print(base)
    break
  
