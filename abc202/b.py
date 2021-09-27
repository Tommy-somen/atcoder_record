s = input()
sr = list(s[::-1])

for i in range(len(sr)):
  if sr[i] == "6":
    sr[i] = "9"
    continue
  elif sr[i] == "9":
    sr[i] = "6"
    continue
print("".join(sr))
