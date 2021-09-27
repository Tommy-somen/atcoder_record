import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

l = []
a, b,num = 0,0,0

for m in range(1,n+1):
	l.append(m)

for i in itertools.permutations(l):
	num += 1
	if i == p:
		a = num
	if i == q:
		b = num
print(abs(a-b))
