n,m = list(map(int,input().split()))
broken_stairs = []

for _ in range(m):
  s = int(input())
  broken_stairs.append(s)
  
stair = [0 for DP in range(n+1)]
stair[0] = 1

for k in broken_stairs:
  stair[k] = -float("inf")

cnt = 0

if stair[1] != -float("inf"):
  stair[1] = 1

for i in range(2,n+1):
  if stair[i] == -float("inf"):
    continue

  if (stair[i-1] != -float("inf")):# and (stair[i-1] + 1 == i):
    stair[i] += stair[i-1]

  if (stair[i-2] != -float("inf")):# and (stair[i-2] + 2 == i):
    stair[i] += stair[i-2]

  #stair[i] = tmp1+tmp2
  #print(stair)

print(stair[n]%1000000007)
