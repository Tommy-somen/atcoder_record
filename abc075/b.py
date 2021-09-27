from collections import deque
h,w = list(map(int,input().split()))
#入力ボードに対して、ゼロパディングを施す
pad = list("."*(w+2))
b = []
board = deque(b)
board.append(pad)
for _ in range(h):
    s = "."+input()+"."
    board.append(list(s))
board.append(pad)

for i in range(1,h+1):
  for j in range(1,w+1):
    if board[i][j] == ".":
      board[i][j] = 0
      if board[i][j-1] == "#":
        board[i][j] += 1
      if board[i-1][j-1] == "#":
        board[i][j] += 1
      if board[i-1][j] == "#":
        board[i][j] += 1
      if board[i-1][j+1] == "#":
        board[i][j] += 1
      if board[i][j+1] == "#":
        board[i][j] += 1
      if board[i+1][j+1] == "#":
        board[i][j] += 1
      if board[i+1][j] == "#":
        board[i][j] += 1
      if board[i+1][j-1] == "#":
        board[i][j] += 1

board.pop()
board.popleft()

for m in board:
  m.pop(0)
  m.pop(-1)

for k in board:
  k = list(map(str,k))
  k = "".join(k)
  print(k)
