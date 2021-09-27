n = int(input())

total = 2025
sub = total - n

ans = []

for i in range(1,10):
  for j in range(1,10):
    if sub == i*j:
      ans.append([i,j])

for k in ans:
  print(k[0],"x",k[1])
