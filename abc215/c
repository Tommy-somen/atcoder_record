import itertools

input_data = list(map(str,input().split()))
s = list(input_data[0])
num = int(input_data[1])

index = 0
target = num-1
box = []

s.sort()

for pattern in itertools.permutations(s):
  box.append("".join(pattern))
  
no_dup_box = list(set(box))

print(str(no_dup_box[target]))
