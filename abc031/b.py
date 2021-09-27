l,m = list(map(int,input().split()))
n = int(input())
log = []
for _ in range(n):
  s = int(input())
  log.append(s)
  
result = []

for i in range(n):
  if log[i] < l:
    result.append(l-log[i])
  elif m < log[i]:
    result.append(-1)
  elif l <= log[i] <= m:
    result.append(0)
  else:
    result.append(-1)
    
for j in result:
  print(j)
