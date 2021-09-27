import sys
 
n,x = list(map(int,input().split()))
vp = [list(map(int,input().split())) for _ in range(n)]
 
cap = 0
cap_r = 0
cnt = 0
 
for i in vp:
  cnt += 1
  cap += (i[0]*i[1])
  if cap > x*100:
    print(cnt)
    sys.exit()

print(-1)
