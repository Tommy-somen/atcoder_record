N,T = map(int,input().split())
ct = [list(map(int,input().split())) for j in range(N)]
box = []
for i in range(N):
	if ct[i][1] <= T:
		box.append(ct[i])
if box ==[]:
	print("TLE")
else:
	box.sort(key=lambda x:x[0])
	print(box[0][0])
		
