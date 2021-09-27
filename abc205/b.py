n = int(input())
a = list(map(int,input().split()))

a_r = sorted(a)
#print(a_r)

flg = True

for i in range(1,n+1):
  #print(a_r[i-1],i)
  if a_r[i-1] != i:
    flg = False
    
if flg:
  print("Yes")
else:
  print("No")
