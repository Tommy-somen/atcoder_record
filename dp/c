n = int(input())
c = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*3 for l in range(n)]

#初期化
dp[0][0],dp[0][1],dp[0][2] = c[0][0],c[0][1],c[0][2]

for i in range(1,n):
  for j in range(3):
    for k in range(3):
      if j != k:
        dp[i][j] = max(dp[i][j],dp[i-1][k]+c[i][j])


print(max(dp[-1]))
