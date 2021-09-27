h,w = list(map(int,input().split()))
board = [list("#"*(w+2))]
for _ in range(h):
  s = "#" + input() + "#"
  board.append(list(s))
board.append(list("#"*(w+2)))

cnt = 0

for i in range(1,h+1):
  for j in range(1,w+1):
    if board[i][j] == ".":
      board[i][j] = "#"
      if board[i][j-1] == ".":
        cnt += 1
      if board[i+1][j] == ".":
        cnt += 1
      if board[i][j+1] == ".":
        cnt += 1
      if board[i-1][j] == ".":
        cnt += 1

print(cnt)
