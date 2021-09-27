import sys
 
#ビンゴカードのデータを受け取る
bingo = [list(map(int,input().split())) for _ in range(3)]
#インプットされるビンゴナンバーの数
n = int(input())
#入力されるビンゴナンバー
num = [int(input()) for k in range(n)]
 
#ビンゴナンバーがカードにあった場合、数字→"#"とする
for i in range(3):
  for t in range(3):
    for j in num:
      if j == bingo[i][t]:
        bingo[i][t] = "#"
        
#ビンゴカードを行ごとに分割する
a = bingo[0]
b = bingo[1]
c = bingo[2]
 
#ビンゴ数をカウントする
cnt = 0
 
#行ごとにビンゴか確かめる
for m in bingo:
  if m.count("#") == 3:
    print("Yes")
    sys.exit()

#列ごとにビンゴか確かめる
for l in range(3):
  if a[l] == "#" and b[l] == "#" and c[l]== "#":
    print("Yes")
    sys.exit()
    
#左上から右下に向けてビンゴか確かめる
if a[0] == "#" and b[1] == "#" and c[2]== "#":
    print("Yes")
    sys.exit()

#右上から左下に向けてビンゴか確かめる
if a[2] == "#" and b[1] == "#" and c[0]== "#":
    print("Yes")
    sys.exit()

print("No")
