n,x = list(map(int,input().split()))
a = list(map(int,input().split()))

cnt = 1
ans = 0

for i in range(n):
  
  if cnt%2 == 0: 
    a[i] -= 1
  cnt += 1
  
  ans += a[i]

if ans <= x:
  print("Yes")
else:
  print("No")
