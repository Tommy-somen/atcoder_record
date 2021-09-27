import math

n = int(input())

r = []
for _ in range(n):
  s = int(input())
  r.append(s)
  
r.sort()

r_r = r[::-1]

flg = 0
ans = 0

for i in range(n):
  flg += 1
  if flg%2 == 0:
    ans -= (r_r[i]**2)
  else:
    ans += (r_r[i]**2)
    
print(ans*(math.pi))
