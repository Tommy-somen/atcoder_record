A,B,C,D = map(int,input().split())
if (A+B) == (C+D):
  print("Balanced")
elif (A+B) < (C+D):
  print("Right")
else:
  print("Left")
