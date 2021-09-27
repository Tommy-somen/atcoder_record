n = int(input())
h = list(map(int,input().split()))

dp = [0]*(n)
#足場を移動しない場合の初期値
dp[0] = 0
#一番目の足場に移動する場合は0→1の１通りのなので定義する。
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
  one_step = abs(h[i]-h[i-1])+dp[i-1]
  two_step = abs(h[i]-h[i-2])+dp[i-2]
  dp[i] = min(one_step,two_step)
  
print(dp[n-1])
