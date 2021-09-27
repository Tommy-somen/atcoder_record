n = int(input())

ans = []

for i in range(120):
  if n == 0:
    break

  if n%2 == 0:
    ans.append("B")
    n //= 2
  else:
    ans.append("A")
    n -= 1

ans.reverse()

print("".join(ans))
