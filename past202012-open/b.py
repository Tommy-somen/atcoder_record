n = int(input())
s = list(input())
t = []

for i in range(n):
  if s[i] in t:
    t.remove(s[i])
  t.append(s[i])
  
tj = "".join(t)

print(tj)
