import sys
A,B = map(int,input().split())
if B == 1:
  print(0)
  sys.exit()
  
for i in range(1,20):
  if (1+(A-1)*i) >= B:
    print(i)
    sys.exit()
