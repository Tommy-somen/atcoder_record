import collections

n = int(input())

s = list(input())

below_we = collections.Counter(s)
over_we = {"W":0,"E":0}

min_people = float("inf")

for i in range(n):
  if s[i] == "W":
    below_we["W"] -= 1
    if min_people > (below_we["E"]+over_we["W"]):
      min_people = (below_we["E"]+over_we["W"])
    over_we["W"] += 1
  else:
    below_we["E"] -= 1
    if min_people > (below_we["E"]+over_we["W"]):
      min_people = (below_we["E"]+over_we["W"])
    over_we["E"] += 1
    
print(min_people)
