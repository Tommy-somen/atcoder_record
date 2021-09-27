n = int(input())
s = list(input())

index = 0

for i in range(n):
  index += 1
  if s[i] == "1":
    break
    
if index%2 != 0:
  print("Takahashi")
else:
  print("Aoki")
