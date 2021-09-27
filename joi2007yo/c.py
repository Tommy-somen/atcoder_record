s = list(input())
L = len(s)

alp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

ans = []

for i in s:
  Num = alp.index(i)
  if Num - 2 <= 0:
    T = 26 + (Num - 3)
  else:
    T = (Num - 3)

  ans.append(alp[T])
  
print("".join(ans))
