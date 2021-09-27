import math

n = int(input())
a = list(map(int,input().split()))

numlist = {}

l = min(1000,len(a))

for i in range(l):

  num = 1

  while(num <= int(math.sqrt(a[i]))):
    
    if a[i]%num == 0:
      
      if numlist.get(num) == None:
        numlist[num] = 1
      else:
        numlist[num] += 1 
        
      if num != (a[i]//num):
 
        if numlist.get(a[i]//num) == None:
          numlist[a[i]//num] = 1
        else:
          numlist[a[i]//num] += 1
    num += 1

ans = [1]

for key,val in numlist.items():
  if val >= l-1:
    ans.append(key)

print(max(ans))
