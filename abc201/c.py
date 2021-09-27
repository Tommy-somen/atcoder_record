#リストの直積などに関して有用なモジュール
from itertools import product

s = list(input())

exist = []
not_exist = []
cnt = 0

for i in range(10):
  if s[i] == "o":
    exist.append(i)
  if s[i] == "x":
    not_exist.append(i)

exist = set(exist)
not_exist = set(not_exist)

#productを利用して、0~9までの数字を、４桁繰り返して0000~9999を表現する
for prod in product(range(10),repeat=4):
  """
(0, 0, 0, 0)
(0, 0, 0, 1)
(0, 0, 0, 2)
.
.
(9,9,9,9)
"""
  prod = set(prod)
  #集合set()は、>=により、部分集合かどうかを判定できる。＆.isdisjointは共通要素がないときにTrueを返す
  if (prod >= exist) and prod.isdisjoint(not_exist):
    #つまり、"o"の要素＋αが全て含まれている　かつ　そこに"x"の要素はない　ことを判定すると、？の処理もできる
    cnt += 1

print(cnt)
    
