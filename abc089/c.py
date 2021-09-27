import itertools
from collections import Counter
n = int(input())
s = [input()[0] for _ in range(n)]
cnt = Counter(s)
#print(cnt)

ans = 0
for x,y,z in itertools.combinations("MARCH",3):
 # print(x,y,z)
  ans += cnt[x]*cnt[y]*cnt[z]
  #print(cnt[x],cnt[y],cnt[z])
        
print(ans)
