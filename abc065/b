import sys

n = int(input())
light = [0]
flg = [0]

for _ in range(n):
	num = int(input())
	light.append(num)
	flg.append(True)

judge = flg[1]
pnt = 1
cnt = 0

while(judge==True):
	
	if flg[pnt]:
		cnt += 1
		
		flg[pnt] = False
		pnt = light[pnt]
		judge = flg[pnt]
		

		if pnt == 2:
			print(cnt)
			sys.exit()

print(-1)
