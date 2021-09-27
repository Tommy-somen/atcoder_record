#copyのインポート
import copy

h,w = list(map(int,input().split()))
#入力ボードに対して、ゼロパディングを施す
pad = list("."*(w+2))
b = []
board = []
#先頭行のパディング
board.append(pad)
#入力時に左と右にパディング
for _ in range(h):
    s = "."+input()+"."
    board.append(list(s))
#最終行にパディング
board.append(pad)

ans = copy.deepcopy(board)

#"."部分を0に置換し、周辺に"#"があればインクリメント
for i in range(1,h+1):
  for j in range(1,w+1):
    if board[i][j] == "#":
      ans[i][j] = 1
    else:
      ans[i][j] = 0
      
for m in range(1,h+1):
  for l in range(1,w+1):    
    if board[m][l-1] == "#":
      ans[m][l] += 1
    if board[m-1][l-1] == "#":
      ans[m][l] += 1
    if board[m-1][l] == "#":
      ans[m][l] += 1
    if board[m-1][l+1] == "#":
      ans[m][l] += 1
    if board[m][l+1] == "#":
      ans[m][l] += 1
    if board[m+1][l+1] == "#":
      ans[m][l] += 1
    if board[m+1][l] == "#":
      ans[m][l] += 1
    if board[m+1][l-1] == "#":
      ans[m][l] += 1

#パディングを排除する
ans.pop()
ans.pop(0)

for m in ans:
  m.pop(0)
  m.pop(-1)

#文字列として結合させ、出力する
for k in ans:
  k = list(map(str,k))
  k = "".join(k)
  print(k)
