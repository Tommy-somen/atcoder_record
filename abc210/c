n,k = list(map(int,input().split()))
c = list(map(int,input().split()))

cnt = 0
box = []
index = 0
check = {}
tmp = []

for i in range(k):
  if check.get(c[i]) == None:
    check[c[i]] = 1
    tmp.append(c[i])
  else:
    check[c[i]] += 1

head = len(tmp)
box.append(head)

for j in range(1,n-k+1):
  check[c[j-1]] -= 1
  if check[c[j-1]] <= 0:
    check[c[j-1]] = None
    head -= 1
  if check.get(c[j+k-1]) == None:
    check[c[j+k-1]] = 1
    head += 1
  else:
    check[c[j+k-1]] += 1
  #print(c[j+k-1])

  box.append(head)

print(max(box))
