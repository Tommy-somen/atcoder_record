#permutationsモジュールのインポート
from itertools import permutations
import copy
import sys

n = int(input())
s = input()
#文字列sの逆文字列を作成する
s_r = copy.copy(list(s))
s_r.reverse()
s_r = "".join(s_r)

#文字列Tの総順列リストを作成する
T = list(permutations(s,n))

#条件を満たすかを確認する
for t in T:
  t = "".join(t)
  if t != s:
    if t != s_r:
      print(t)
      sys.exit()
print("None")
