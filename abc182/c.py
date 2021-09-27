import sys
n = input()
nn = list(map(int,list(n)))

total = int(n)#sum(n)
cnt = 0

if sum(nn)%3 == 0:
  print(cnt)
  sys.exit()

mod = []
for i in nn:
  mod.append(i%3)
mod.sort(reverse=True)
  
while len(mod) != 0:
  cnt += 1
  L = len(mod)
  for j in range(L):
    tmp = total - mod[j]
    if (tmp%3 == 0) and (len(mod)>1):
      print(cnt)
      sys.exit()
  total -= mod[0]
  mod.pop(0)


if len(mod) == 0:
  print(-1)
else:
  print(cnt)
