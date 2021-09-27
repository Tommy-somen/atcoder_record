a = list(input())

length = len(a)

if length > 1:
  print(a[0])
else:
  if a[0] == "a":
    print(-1)
  else:
    print(chr(ord(a[0])-1))
