n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

am = max(a)
bm = min(b)

s = bm - am

if s >= 0:
  print(s+1)
else:
  print(0)
