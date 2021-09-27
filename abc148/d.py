n = int(input())
a = list(map(int,input().split()))
inx,cnt = 1,0
for i in range(n):
  if a[i] != inx:
    cnt += 1
  else:
    inx += 1
if n == cnt:
  print(-1)
else:  
  print(cnt)
