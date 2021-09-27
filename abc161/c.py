import sys
n,k = map(int,input().split())
if n%k == 0:
	print(0)
	sys.exit()
num = n - k*(n//k)
abnum = abs(num - k)
print(min(num,abnum))
