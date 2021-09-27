import math
a,b = map(str,input().split())
N = int(a+b)
hN = math.ceil(math.sqrt(N))
if hN**2 == N:
  print("Yes")
else:
  print("No")

