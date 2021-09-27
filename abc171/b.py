N,K = map(int,input().split())
P = list(map(int,input().split()))
sum,cnt = 0,0
for i in range(K):
  sum += sorted(P)[i]
print(sum)
