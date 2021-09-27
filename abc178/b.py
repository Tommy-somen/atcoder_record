N = list(map(int,input().split()))
x = []
for i in range(2):
  for j in range(2,4):
    n = N[i]*N[j]
    x.append(n)
print(max(x))
