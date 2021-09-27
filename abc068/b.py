import sys
N = int(input())
for i in range(0,7):
	if N == 1:
		print(1)
		sys.exit()
	elif N >= 64:
		print(64)
		sys.exit()
	elif N < 2**i:
		print(2**(i-1))
		sys.exit()
