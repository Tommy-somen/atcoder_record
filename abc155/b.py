N = int(input())
A = list(map(int,input().split()))

#A内の奇数を0にする
for i in range(len(A)):
	if A[i]%2 != 0:
		A[i] = 0
#A内偶数をチェックする
for t in range(len(A)):
	if A[t] > 0:
		if A[t]%3 == 0 or A[t]%5 == 0:
			A[t] = 0
print("APPROVED" if sum(A) == 0  else "DENIED")

