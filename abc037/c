n,k = list(map(int,input().split()))
a = list(map(int,input().split()))

pre = sum(a[:k])

total = sum(a[:k])

for i in range(1,(n-k)+1):
  total += (pre - a[i-1] + a[i+(k-1)])
  pre = (pre - a[i-1] + a[i+(k-1)])

print(total)
