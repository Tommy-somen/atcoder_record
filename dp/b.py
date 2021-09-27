n,K = list(map(int,input().split()))
h = list(map(int,input().split()))

dp = [float("inf")]*(n)
#足場を移動しない場合の初期値
dp[0] = 0
#一番目の足場に移動する場合は0→1の１通りのなので定義する。
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
  for k in range(1,K+1):
    K_step = abs(h[i]-h[i-k])+dp[i-k]
    dp[i] = min(dp[i],K_step)

print(dp[n-1])
