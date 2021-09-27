import copy

n,k = list(map(int,input().split()))

def fx(kap):
  
  nstr = list(str(kap))
  g1 = copy.copy(nstr)
  g1 = list(map(int,g1))
  g1 = sorted(g1,reverse=True)
  g1 = list(map(str,g1))
  g1 = "".join(g1)
  g1 = int(g1)
  #print(g1)

  g2 = copy.copy(nstr)
  g2 = list(map(int,g2))
  g2 = sorted(g2)
  g2 = list(map(str,g2))
  g2 = "".join(g2)
  g2 = int(g2)
  #print(g2)
  
  global n
  n = g1 - g2
  return n

ans = n

for i in range(k):
  ans = fx(ans)

print(ans)
