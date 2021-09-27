import sys
readline = sys.stdin.readline
A, B, C, K = map(int,readline().split())
count = 0

if A >= K:
	print(K)
	sys.exit()

while(K>0):
	if A != 0:
		count += A
		K -= A
		A = 0
	elif B != 0:
		K -= B
		B = 0
	else:
		count -= K
		K = 0
			
print(count)
