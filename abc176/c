n = int(input())

step = list(map(int,input().split()))

max_height = step[0]
ans = 0

for i in range(1,n):
  if max_height >= step[i]:
    ans += (max_height-step[i])
  else:
    max_height = step[i]

print(ans)    
