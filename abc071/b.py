import sys
s = list(input())
for i in range(0,26):
  if not chr(97+i) in s:
    print(chr(97+i))
    sys.exit()
print("None")
