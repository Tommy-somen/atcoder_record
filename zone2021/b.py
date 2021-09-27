n,d,h = list(map(int,input().split()))
dh = [list(map(int,input().split())) for _ in range(n)]

mx,my = 0,0
ans = 0

for j in dh:
  mx,my = j[0],j[1]
  katamuki = (h-my)/(d-mx)
  high = my-(mx*katamuki)
  ans = max(ans,high)
  
print(max(0,ans))
