import sys

x = str(input())
xl = list(x)
ans = []

if xl.count('.') == 0:
	print(int(x))
	sys.exit()
else:
	for i in xl:
		if i != '.':
			ans.append(i)
		else:
			break

ans_join = (''.join(ans))
print(int(ans_join))
