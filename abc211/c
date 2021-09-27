s = list(input())

cho = ["c","h","o","k","u","d","a","i"]

dp = [[0 for _ in range(len(cho)+1)] for __ in range(len(s)+1)]

for i in range(len(cho)+1):
  dp[0][i] = 0

for j in range(len(s)+1):
  dp[j][0] = 1

for i in range(len(s)):
  #print(i)
  for j in range(len(cho)):
    if s[i] != cho[j]:
      dp[i][j+1] = dp[i-1][j+1]
    else:
      dp[i][j+1] = (dp[i-1][j]+dp[i-1][j+1])%(10**9+7)
    #print(dp)

print(dp[len(s)-1][8])
