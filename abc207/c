n = int(input())

t = []
l = []
r = []

for k in range(n):
  T,L,R = list(map(int,input().split()))
  t.append(T)
  l.append(L)
  r.append(R)
  
for pre in range(n):
  if t[pre] == 2:
    r[pre] -= 0.01
  elif t[pre] == 3:
    l[pre] += 0.01
  elif t[pre] == 4:
    r[pre] -= 0.01
    l[pre] += 0.01

cnt = 0

for i in range(n-1):
  for j in range(i+1,n):
    if l[j] <= l[i] <= r[j] <= r[j]:
      cnt += 1
    elif l[i] <= l[j] <= r[j] <= r[i]:
      cnt += 1
    elif l[i] <= l[j] <= r[i] <= r[j]:
      cnt += 1
    elif l[j] <= l[i] <= r[i] <= r[j]:
      cnt += 1

print(cnt)
