n = int(input())
lr = [list(map(int,input().split())) for l in range(n)]
ans = 0
for i in range(len(lr)):
  ans += (lr[i][1] - lr[i][0])+1
print(ans)
