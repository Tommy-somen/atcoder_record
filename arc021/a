grid = []

#番兵つき平面を作成
grid.append(["#"]*6)
for _ in range(4):
  s = list(map(int,input().split()))
  s.insert(0,"#")
  s.append("#")
  grid.append(s)
grid.append(["#"]*6)

Flg = False

for i in range(1,5):
  for j in range(1,5):
    if (grid[i-1][j] == grid[i][j]):
      Flg = True
    elif (grid[i+1][j] == grid[i][j]):
      Flg = True
    elif (grid[i][j-1] == grid[i][j]):
      Flg = True
    elif (grid[i][j+1] == grid[i][j]):
      Flg = True

if Flg:
  print("CONTINUE")
else:
  print("GAMEOVER")
