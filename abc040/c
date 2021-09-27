n = int(input())
tree = list(map(int,input().split()))

cost = [float("inf") for _ in range(n)]
cost[0] = 0
cost[1] = abs(tree[1]-tree[0])

for i in range(2,n):
  one_sub = cost[i-1]+abs(tree[i-1]-tree[i])
  two_sub = cost[i-2]+abs(tree[i-2]-tree[i])
  cost[i] = min(one_sub,two_sub)

print(cost[n-1])
