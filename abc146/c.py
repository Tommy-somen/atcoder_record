import sys
a,b,x = map(int,input().split())
l = len(list(str(x)))
tmp,ans =[],[]
for i in range(1,l+1):
	tmp.append(int((x/a)-(b*i)/a))
for j in range(len(tmp)):
	if a*tmp[j]+b*len(list(str(tmp[j]))) <= x:
		ans.append(tmp[j])
if max(ans) >= 10**9:
	print(10**9)
	sys.exit()
elif ans == []:
	print(0)
	sys.exit()
print(max(ans) if max(ans) > 0 else 0)
