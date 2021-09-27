s = list(input())

A = []
Z = []

for i in range(len(s)):
  if s[i] == "A":
    A.append(i)
  elif s[i] == "Z":
    Z.append(i)

start = min(A)
last = max(Z)

ans = last - start
print(ans+1)
