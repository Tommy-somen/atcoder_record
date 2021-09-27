n,m,q = list(map(int,input().split()))
uv = [list(map(int,input().split())) for UV in range(m)]
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for query in range(q)]

top = [[] for _ in range(n+1)]

for N in uv:
  top[N[0]].append(N[1])
  top[N[1]].append(N[0])


color = []

for i in s:
  color.append(c[i[1]-1])

  if i[0] == 1:
    for j in top[i[1]]:
      c[j-1] = c[i[1]-1]
  else:
    c[i[1]-1] = i[2]

for k in color:
  print(k)
