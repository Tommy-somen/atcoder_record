a,b,c = list(map(int,input().split()))
x = [a,b,c]
x.sort()

if x[1] == a:
  print("A")
elif x[1] == b:
  print("B")
else:
  print("C")
