n = int(input())

plots = []
for _ in range(n):
  x,y = list(map(int,input().split()))
  plots.append([x,y])

cnt = 0

for i in range(n):
  for j in range(i,n):
    try:
      if -1 <= ((plots[j][1] - plots[i][1])/(plots[j][0] - plots[i][0])) <= 1:
        cnt += 1
    except ZeroDivisionError:
      continue
      
print(cnt)
