import sys
s = list(input())

for o in range(1):
  if int(s[o]) == 7 and int(s[o+1]) == 8 and int(s[o+2]) == 9 and int(s[o+3]) == 0:
    print("Weak")
    sys.exit()

for j in range(1):
  if int(s[j]) == 8 and int(s[j+1]) == 9 and int(s[j+2]) == 0 and int(s[j+3]) == 1:
    print("Weak")
    sys.exit()
    
for k in range(1):
  if int(s[k]) == 9 and int(s[k+1]) == 0 and int(s[k+2]) == 1 and int(s[j+3]) == 2:
    print("Weak")
    sys.exit()

ini = s[0]
if s.count(ini) == 4:
  print("Weak")
  sys.exit()
     
if (((int(s[0])+1) == int(s[1])) and ((int(s[1])+1) == int(s[2])) and ((int(s[2])+1) == int(s[3]))):
    print("Weak")
else:
  print("Strong")
