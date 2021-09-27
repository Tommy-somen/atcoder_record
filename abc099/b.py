a,b = map(int,input().split())
ans = 0
N = b - a
for i in range(1,N):
  ans += i
print(ans - a)
  
