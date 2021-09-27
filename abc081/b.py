n = int(input())
A = list(map(int,input().split()))

ans = []

for i in A:
  cnt = 0
  for j in range(34):
    if ((i>>j)&1):
      ans.append(cnt)
      break
    else:
      cnt += 1

minimam = min(ans)
print(minimam)
