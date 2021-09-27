s = list(input())

four = s.pop(3)

flg = True
for i in s:
  if not i.isdigit():
    flg = False
if not four == "-":
  flg = False

if flg:
  print("Yes")
else:
  print("No")
