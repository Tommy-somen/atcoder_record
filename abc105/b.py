import sys
N = int(input())
for i in range(50):
  for j in range(30):
    if i*4 + j*7 == N:
      print("Yes")
      sys.exit()
print("No")
    
