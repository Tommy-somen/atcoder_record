s = list(input())
box = []
cnt = 0
for i in s:
	if i == 'R':
		cnt += 1
	else:
		box.append(cnt)
		cnt = 0
box.append(cnt)
print(max(box))
