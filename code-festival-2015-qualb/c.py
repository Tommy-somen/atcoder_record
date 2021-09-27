n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

flg = True

for i in range(m):
  try:
    if b[i] > a[i]:
      flg = False
  except IndexError:
    flg = False
    break
    
if flg:
  print("YES")
else:
  print("NO")
