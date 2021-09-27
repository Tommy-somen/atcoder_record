n = int(input())
T = list(map(int,input().split()))
m = int(input())
p,x = [],[]
for PX in range(m):
  P,X = list(map(int,input().split()))  
  p.append(P)
  x.append(X)

for i in range(m):
  ans = 0
  pi = p[i]
  xi = x[i]
  tmp = T[pi-1]
  T[pi-1] = xi

  for j in range(n):
    ans += T[j]

  T[pi-1] = tmp
  print(ans)
