N,K = map(int,input().split())
d = []
A = []
count = [0]*N
count.insert(0,'X')

for i in range(K):
	d.append(input())
	A.append(list(map(int,input().split())))
	
for s in range(len(A)):
	for t in range(len(A[s])):
		count[A[s][t]] += 1

print(count.count(0))
