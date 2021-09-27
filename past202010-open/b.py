x,y = list(map(int,input().split()))
n = 2
if y == 0:
  print("ERROR")
else:
  ans = x/y
  ans = int(ans*10**2)/10**2
  print("{:.2f}".format(ans))
