import sys

s = input()
sl = list(s)

if s == "0":
  print("Yes")
  sys.exit()

fz,bz = 0,0
#front処理
for i in range(len(sl)):
  if sl[i] == "0":
    sl.pop(0)
    fz += 1
  else:
    break
#back処理
for j in range(len(sl)):
  if sl[-1] == "0":
    sl.pop(-1)
    bz += 1
  else:
    break

front = "".join(sl)
sl.reverse()
back = "".join(sl)

if front == back and bz>=fz:
  print("Yes")
else:
  print("No")
