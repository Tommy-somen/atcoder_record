import sys

a,b,c,d = list(map(int,input().split()))

flg = False
cnt = 0

blue = a
red = 0

if blue <= red*d:
  flg = True
  print(0)
  sys.exit()

for i in range(100000):
  cnt += 1
  blue += b
  red += c
  if blue <= red*d:
    flg = True
    break
    
if flg == False:
  print(-1)
else:
  print(cnt)
