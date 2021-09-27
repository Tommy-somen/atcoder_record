n = int(input())

A = list(map(int,input().split()))

cnt = [0 for _ in range(1001)]

for a in A:
  i = 2
  while(i <= a):
    if a%i == 0:
      cnt[i-1] += 1
    i += 1

ans = 0
for cmp in range(len(cnt)):
  if ans <= cnt[cmp]:
    ans = cnt[cmp]
    flg = cmp+1
    
print(flg)
