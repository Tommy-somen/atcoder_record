h,w,n = list(map(int,input().split()))
x,y = [],[]

for _ in range(n):
  X,Y = list(map(int,input().split()))
  x.append(X)
  y.append(Y)

Xdict = {}
Ydict = {}

for i,xa in enumerate(sorted(list(set(x)))):
  Xdict[xa] = i+1
  
for j,ya in enumerate(sorted(list(set(y)))):
  Ydict[ya] = j+1

for k in range(n):
  print(Xdict[x[k]],Ydict[y[k]])
