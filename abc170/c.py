import sys
x,n = list(map(int,input().split()))

if n == 0:
  print(x)
  sys.exit()
else:
  p = list(map(int,input().split()))

max_p = max(p)+100
not_p = [i for i in range(0,max_p) if not i in p]

num = 10**9
ans = []

for j in not_p:
    num = abs(x-j)
    ans.append([num,j])
  
ans.sort(key=lambda x:x[0])

print(ans[0][1])
