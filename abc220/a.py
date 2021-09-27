a,b,c = list(map(int,input().split()))

for i in range(100000000):
  if a <= c*i <= b:
    print(c*i)
    break
  if c*i > b:
    print(-1)
    break
