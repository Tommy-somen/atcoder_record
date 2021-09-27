import sys

n,x = map(int,input().split())
order = list((map(int,input().split())))

ans = []

for i in range(n):
  if order[i] != x:
    ans.append(order[i])
    
if len(ans) >0:
  ans_s = " ".join(map(str,ans))
  print(ans_s)
else:
  print("")
