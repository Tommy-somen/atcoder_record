import sys
N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]
x = 0
for i in range(N):
  if D[i][0] == D[i][1]:
    x += 1
  else:
    x *= 0
  if x == 3:
    print("Yes")
    sys.exit()
print("No")
