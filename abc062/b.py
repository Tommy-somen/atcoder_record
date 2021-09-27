from collections import deque

h,w = list(map(int,input().split()))

#入力に対して、パディングを施す
pad = list("#"*(w+2))
b = []
board = deque(b)
#先頭行のパディング
board.append(pad)
#入力時に左と右にパディング
for _ in range(h):
  s = "#"+input()+"#"
  board.append(list(s))
#最終行にパディング
board.append(pad)

for i in board:
  i = "".join(i)
  print(i)
