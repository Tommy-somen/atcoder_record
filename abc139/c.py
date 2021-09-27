n = int(input())
h = list(map(int,input().split()))
counter =[]
cnt = 0
for i in range(n-1):
  if h[i] >= h[i+1]:
    cnt += 1
  else:
    counter.append(cnt)
    cnt = 0
counter.append(cnt)
print(max(counter))
