A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
x,y = map(int,input().split())
if x == 2 or y == 2:
  print("No")
elif x in A and y in A:
  print("Yes")
elif x in B and y in B:
  print("Yes")
else:
  print("No")
