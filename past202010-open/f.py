n,k = list(map(int,input().split()))
Sn = [input() for _ in range(n)]
Su = list(set(Sn))

for i in range(len(Su)):
  Su[i] = [Su[i],0]

Sd = dict(Su)

for j in Sn:
  Sd[j] += 1

sorted_Sd = sorted(Sd.items(), key=lambda x:x[1],reverse=True)
items = []
for No in sorted_Sd:
  items.append(No[1])

num = items[k-1]

ans = [q for q, p in Sd.items() if p == num]

if len(ans) >= 2:
  print("AMBIGUOUS")
else:
  print(ans[0])
