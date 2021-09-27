n = int(input())

mini = []

for i in range(1,n+1):
  j = n//i
  sub = abs(i-j)
  mod = n-(i*j)
  mini.append(sub+mod)

print(min(mini))
