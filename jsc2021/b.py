n,m = list(map(int,input().split()))

A = list(map(int,input().split()))
B = list(map(int,input().split()))

common = []

for a in A:
  if not a in B:
    common.append(a)
    
for b in B:
  if not b in A:
    common.append(b)   
    
if len(common) > 0:
  common = list(set(common))

  common.sort()

  ans = " ".join(map(str,common))
  print(ans)
else:
  print("")
