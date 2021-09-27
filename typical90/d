h,w = list(map(int,input().split()))

ROW = []
COLUMN = []
SUM_Matrix = []

for row in range(h):
  ROW_input = list(map(int,input().split()))
  ROW.append(ROW_input)
  SUM_ROW = sum(ROW_input)
  SUM_Matrix.append([SUM_ROW]*w)

for clm in range(w):
  column = 0
  for r in range(h):
    column += ROW[r][clm]
  COLUMN.append(column)

for i in range(h):
  for j in range(w):
    SUM_Matrix[i][j] += COLUMN[j]
    SUM_Matrix[i][j] -= ROW[i][j]

for ANS in SUM_Matrix:
  print(*ANS)
