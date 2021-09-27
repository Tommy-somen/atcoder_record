k,x = map(int,input().split())
c =[]
for i in range(x-k+1,x+k):
  c.append(i)
print(' '.join(map(str,c)))
