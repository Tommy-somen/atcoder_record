A,B,K = map(int,input().split())
if A+B <= K:
	print(0,0)
elif A >= K:
	print(A-K,B)
else:
	print(0,B -(K-A))
