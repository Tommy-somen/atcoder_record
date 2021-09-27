a,b,c,d = map(int,input().split())
if abs(a-c) <= d:
  print("Yes")
else:
  print("Yes" if abs(b-a)<= d and abs(c-b)<= d else "No")
