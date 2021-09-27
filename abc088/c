grid = [list(map(int,input().split())) for _ in range(3)]
	
sum = grid[0][0] + grid[1][1] + grid[2][2]

row = 0

for r in range(3):
	for k in range(3):
		row += grid[r][k]
		
col = 0

i = 0

while(i < 3):
	for j in range(3):
		col += grid[i][j]
	i += 1
	
if (row == col) and (row == (3*sum)):
	print('Yes')
else:
	print('No')
