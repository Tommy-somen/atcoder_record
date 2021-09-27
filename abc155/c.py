n = int(input())
s = [input() for s in range(n)]
dic = {}

for i in range(n):
	if not s[i] in dic:
		dic[s[i]] = 1
	else:
		dic[s[i]] += 1

cnt_max = max(dic.values()) 
ans = []
for j in dic.keys():
	if dic[j] == cnt_max:
		ans.append(j)

ans.sort()

for h in range(len(ans)):
	print(ans[h])
