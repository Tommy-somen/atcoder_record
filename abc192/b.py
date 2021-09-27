import sys

s = input()
slist = list(s)
snum = len(slist)

if snum == 1:
    if slist[0].islower():
        print("Yes")
        sys.exit()
    else:
        print("No")
        sys.exit()

odd = []
even = []

for i in range(1,snum,2):
    even.append(slist[i])

for j in range(0,snum,2):
    odd.append(slist[j])

s_odd = "".join(odd)
s_even = "".join(even)

if s_even.isupper() and s_odd.islower():
  print("Yes")
else:
  print("No")
