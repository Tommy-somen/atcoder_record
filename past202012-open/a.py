import sys
s = list(input())

s.append("0")

cnt = 0

for i in range(3):
    if s[i] == s[i+1] and s[i] == s[i+2]:
      print(s[i])
      sys.exit()

print("draw")
