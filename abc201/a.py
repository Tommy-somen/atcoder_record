import itertools
import sys

lis = list(map(int,input().split()))

answ = list(itertools.permutations(lis))

ans = []

for d in answ:
  ans.append([d[0],d[1],d[2]])

for i in ans:
  if i[2]-i[1] == i[1]-i[0]:
    print("Yes")
    sys.exit()

print("No")
