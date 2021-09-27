import sys
S = input()
T = input()
for i in range(len(S)):
  tmp = S[-1]
  S = tmp + S[:-1]
  if S == T:
    print("Yes")
    sys.exit()
print("No")
