a,b,c = list(map(int,input().split()))

#-a,-b
if (a < 0) and (b < 0) and (c%2 == 0):
  if abs(a) > abs(b):
    print(">")
  elif abs(a) == abs(b):
    print("=")
  else:
    print("<")

elif (a < 0) and (b < 0) and (c%2 != 0):
  if abs(a) > abs(b):
    print("<")
  elif abs(a) == abs(b):
    print("=")
  else:
    print(">")  

#a,-b
elif (a >= 0) and (b < 0) and (c%2 == 0):
  if abs(a) > abs(b):
    print(">")
  elif abs(a) == abs(b):
    print("=")
  else:
    print("<")

elif (a >= 0) and (b < 0) and (c%2 != 0):
  print(">")

#-a,b
elif (a < 0) and (b >= 0) and (c%2 == 0):
  if abs(a) > abs(b):
    print(">")
  elif abs(a) == abs(b):
    print("=")
  else:
    print("<")  

elif (a < 0) and (b >= 0) and (c%2 != 0):
  print("<")

#a,b
elif (a >= 0) and (b >= 0) and (c%2 == 0):
  if abs(a) > abs(b):
    print(">")
  elif abs(a) == abs(b):
    print("=")
  else:
    print("<")  

elif (a >= 0) and (b >= 0) and (c%2 != 0):
  if abs(a) > abs(b):
    print(">")
  elif abs(a) == abs(b):
    print("=")
  else:
    print("<")
