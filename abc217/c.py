n = int(input())
p = list(map(int,input().split()))

order = {}

for i in range(n):
  order[p[i]] = str(i+1)
  
s = []

for j in range(1,n+1):
  s.append(int(order[j]))
  
print(*s)
