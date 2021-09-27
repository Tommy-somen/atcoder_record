import sys
n = input()
digits = len(n)

if digits == 1:
  print(0)
  sys.exit()

if digits%2 != 0: #奇数の時
  s = str(10**(digits-1) -1)
else:
  s = n

digi_s = len(s)//2
pre = int(s[:digi_s])
post = int(s[digi_s:])

if pre > post:
  ans = pre-1
else:
  ans = pre
  
print(ans)
