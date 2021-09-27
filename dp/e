n,W = list(map(int,input().split()))

ws = [0]
vs = [0]

for j in range(n):
  w,v = list(map(int,input().split()))
  ws.append(w)
  vs.append(v)

max_val = sum(vs)

dp = [[float("inf")]*(max_val+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
  for val in range(max_val+1):
    dp[i][val] = min(dp[i][val],dp[i-1][val])
    if val-vs[i] >= 0:
      dp[i][val] = min(dp[i][val],dp[i-1][val-vs[i]]+ws[i])
      
for k in range(max_val+1):
  if W >= dp[n][k]:
    ans = k

print(ans)
