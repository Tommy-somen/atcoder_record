n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

memo = {}

for i in range(n):
  if memo.get(b[c[i]-1]) != None:
    memo[b[c[i]-1]] += 1
  else:
    memo[b[c[i]-1]] = 1
    
ans = 0

for item in a:
  if memo.get(item) != None:
    ans += memo[item]

print(ans)
