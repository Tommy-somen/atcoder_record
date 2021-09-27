import sys
import math
a,b = map(int,input().split())
for i in range(1,1251):
	if math.floor((i*(8/100))) == a and math.floor((i*(10/100))) == b:
		print(i)
		sys.exit()
print(-1)
