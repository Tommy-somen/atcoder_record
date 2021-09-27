n,a,x,y = list(map(int,input().split()))

if n > a:
  print((x*a)+y*(n-a))
else:
  print(x*n)
