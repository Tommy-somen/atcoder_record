N = int(input())
rst = []
for i in range(N):
	S,P = input().split()
	P = int(P)
	rst.append([S,P,i+1])
rst.sort(key=lambda x:x[1],reverse=True)
rst.sort(key=lambda x:x[0])
for j in range(N):
	print(rst[j][2])
