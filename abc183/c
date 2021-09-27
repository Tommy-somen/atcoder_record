"""
1<=n<=8なので全探索で処理できる。
初手は1スタート、かつ、最後は1でゴールするため、
1以外の数字で重複無の順列を考え、その値を用いて計算する。
最後に、順列の最後尾から1に向かう時間を足してkと比較することで
解くことができる。

"""
import itertools

n,k = list(map(int,input().split()))
t = []

for T in range(n):
  s = list(map(int,input().split()))
  t.append(s)
  
numlist = list(range(2,n+1))
cnt = 0

for comb in itertools.permutations(numlist):
  total = t[0][comb[0]-1]
  for i in range(len(comb)-1):
    total += t[comb[i]-1][comb[i+1]-1]
  total += t[comb[-1]-1][0]
  if total == k:
    cnt += 1
         
print(cnt)    
