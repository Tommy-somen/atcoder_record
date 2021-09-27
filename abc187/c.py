import sys

n = int(input())
S = []
for _ in range(n):
  s = input()
  S.append(s)

dct = {}

for item in S:
  if dct.get(item) == None:
    dct[item] = 1
  else:
    pass
  
for check in S:
  if check[0] == "!":
    cmp = check[1:]
  else:
    cmp = "!"+check
    if not dct.get(check) == None:
      if not dct.get(cmp) == None:
        print(check)
        sys.exit()

print('satisfiable')
