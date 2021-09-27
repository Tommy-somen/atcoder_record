import numpy as np

n = int(input())
mtx = [list(map(int,input().split())) for i in range(2)]

mtx = np.array(mtx)
if np.dot(mtx[0],mtx[1]) == 0:
  print("Yes")
else:
  print("No")
