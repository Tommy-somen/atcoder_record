n,x = list(map(int,input().split()))
s = list(input())

cnt = x

for i in range(n):
  if s[i] == "o":
    cnt += 1
  else:
    if cnt > 0:
      cnt -= 1
    else:
      pass

print(cnt)
