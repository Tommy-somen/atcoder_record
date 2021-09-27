import sys
n,m = map(int,input().split())
s_c = [list(map(int,input().split())) for s in range(m)] #0 is s, 1 is c
l = 0
if n == 1:
	n,l = 0,9
elif n == 2:
	n,l =10,99
else:
	n,l = 100,999
for i in range(n,l+1):
	bol = True
	tmp = list(str(i))
	for j in range(m):
		k = s_c[j][0]
		if tmp[k-1] != str(s_c[j][1]):
			bol = False
	if bol:
		print(i)
		sys.exit()
print(-1)
