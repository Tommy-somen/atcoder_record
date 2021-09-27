n = int(input())

#カウントする変数を用意する
cnt = 0

#10進数で７が含まれているものにFalse（最後の処理では0番目は無視して考える）
ten_flg = [True for num in range(n+1)]

#10進数の場合
for ten in range(1,n+1):
  s_ten = list(str(ten))
  if "7" in s_ten:
    ten_flg[ten] = False

#8進数の場合
for eight in range(1,n+1):
  #oct()で８進数に変換する
  s_eight = list(str(oct(eight)))
  if "7" in s_eight:
    ten_flg[eight] = False

#Trueの場合、カウントする
ans = 0
for judge in ten_flg:
  if judge:
    ans += 1

print(ans-1)
